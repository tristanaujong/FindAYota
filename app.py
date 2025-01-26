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
        # with open("data/vehicles.json") as d:
        #     vehicles = json.load(d)
        
        # compute points
        vehicle_point_map = compute_points(user_data) # dict with computed points for each model

        # get top-matched cars


        return render_template("results.html", matches = vehicle_point_map) 
       
    return render_template("form.html", traits = traits_to_ask) # will be an array

# code in compute vehicle points function here
def compute_points(u_data):

    
    return None

if __name__ == "__main__":
    app.run(debug=True)