from flask import Flask, render_template, request
import json
from finance import Finance
from utils.data_parser import parse_vehicles
from vehicle_info import Vehicle

app = Flask(__name__)

# make a function that instantiates a hashmap from json file
# { "corolla" : point }
def create_map():
    vehicle_point_map = {}
    with open("data/vehicles.json") as v:
        car_info = json.load(v)
    car_list = parse_vehicles(car_info) # list of cars
    # now make the hashset with model as key and points as value
    for car in car_list:
        vehicle_point_map.update({car.get_model():0})
    # print(vehicle_point_map)
    return vehicle_point_map

vehicle_point_map = create_map()

traits_to_ask = ["body_style", "drivetrain", "mpg", "engine"]

@app.route("/")
def home():
    return render_template("home.html", title = "FindAYota - Home")

@app.route("/about")
def about():
    return render_template("about.html", title = "FindAYota - About")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST": # user clicks submit
        user_data = request.form.to_dict()  # Collect user data
        
        # load data
        with open("data/vehicles.json") as d:
            vehicles = json.load(d)
        
        # compute points
        vehicle_point_map = compute_points(user_data, vehicle_point_map, vehicles) # dict with computed points for each model

        # get top-matched cars
        top_cars = get_top_percents(vehicle_point_map)

        return render_template("results.html", matches = top_cars) 
       
    return render_template("form.html", traits = traits_to_ask) # will be an array

# code in compute vehicle points function here
# hierarchy
# Engine -> Body -> DriveTrain -> MPG
# 50 -> 25 -> 10 -> 5
def compute_points(u_data, v_map, cars): # u_data is a dict --- ["body_style", "drivetrain", "mpg", "engine"]
    hierarchy = {
        "engine" : 50,
        "body_style" : 25,
        "drivetrain" : 10,
        "mpg" : 5
    }

    for v_name, current_pts in v_map.items():
        vehicle_traits = cars[v_name]

        for trait, pts in hierarchy.items():
            if trait in u_data:
                if vehicle_traits.get(trait) == u_data[trait]:
                    v_map[v_name] += pts

    return v_map

def get_top_percents(v_map): #return dictionary with top 3 cars and their percentage
    sort_cars = sorted(v_map.items(), key=lambda x: x[1], reverse=True)
    top_3 = sort_cars[:3]
    sum_top_3 = sum(points for c,points in top_3)
    top_3_map = {
        car: round((points/sum_top_3) * 100, 2)
        for car, points in top_3
    }

    return top_3_map

if __name__ == "__main__":
    app.run(debug=True)