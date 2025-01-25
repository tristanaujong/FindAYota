from flask import Flask, render_template, request
import json
from finance import Finance
from utils.data_parser import parse_vehicles
from vehicle_info import Vehicle

app = Flask(__name__)

# make a function that instantiates a hashmap from json file

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


@app.route("/")
def home():
    return render_template("home.html", title = "FindAYota - Home")

@app.route("/about")
def about():
    return render_template("about.html", title = "FindAYota - About")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        user_data = request.form  # Collect user data
        # load vehicle data
            # with open("data/vehicles.json") as f:
            #   vehicles = json.load(f) <- this is how to load it in
        # compute vehicle points
            # call a function here that will return a hashmap with car to points pairs
        # Pass matched vehicles to the results page
        return render_template("results.html", matches=vehicle_point_map)    #  is the hashmap returned by the "compute vehicle points" function
    return render_template("form.html")

# code in compute vehicle points function here
def compute_points(vehicle_points):

    
    return None

if __name__ == "__main__":
    app.run(debug=True)