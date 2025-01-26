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
    car_real_info = car_info.get("vehicles", [])
    # print(car_real_info)
    car_list = parse_vehicles(car_real_info)  # list of cars
    print("PRINTING DA LISTTTT")
    print(car_list)
    
    # Standardize the car model names to lowercase and strip any extra spaces
    for car in car_list:
        model_name = car.get_model().strip()  # normalize the model name
        vehicle_point_map.update({model_name: 0})
        
    return vehicle_point_map

# Create the global vehicle_point_map variable
vehicle_point_map = create_map()

traits_to_ask = ["body_style", "drivetrain", "engine"]

@app.route("/")
def home():
    return render_template("home.html", title="FindAYota - Home")

@app.route("/form", methods=["GET", "POST"])
def form():
    global vehicle_point_map  # Declare vehicle_point_map as global to modify it
    print("form accessedd")
    if request.method == "POST":  # user clicks submit
        user_data = request.form.to_dict()  # Collect user data
        print(user_data)
        
        # Load data from the JSON file
        with open("data/vehicles.json") as d:
            vehicles = json.load(d)
        
        # Compute points (this will update the global vehicle_point_map)
        vehicle_point_map = compute_points(user_data, vehicle_point_map, vehicles)  # dict with computed points for each model

        # Get top-matched cars
        top_cars = get_top_percents(vehicle_point_map)

        return render_template("results.html", matches=top_cars, cars=vehicles)

    return render_template("form.html", traits=traits_to_ask)  # will be an array

# code in compute vehicle points function here
# hierarchy
# Engine -> Body -> DriveTrain -> MPG
# 50 -> 25 -> 10 -> 5
def compute_points(u_data, v_map, cars):
    # print("THE CARS")
    # print(cars) -- 'vehicles' big list
    hierarchy = {
        "engine": 50,
        "body_style": 50,
        "drivetrain": 10
    }

    for v_name, current_pts in v_map.items():
        # Normalize the car name to lowercase to avoid KeyError
        v_name_normalized = v_name.strip()  # Normalize to lower case and strip spaces
        if v_name_normalized not in cars:
            print(f"Warning: {v_name_normalized} not found in cars")
            continue
        
        vehicle_traits = cars[v_name_normalized]  # Get the vehicle traits using the normalized name

        for trait, pts in hierarchy.items():
            if trait in u_data:
                if vehicle_traits.get(trait) == u_data[trait]:
                    v_map[v_name] += pts

    return v_map


def get_top_percents(v_map):  # return dictionary with top 3 cars and their percentage
    # Sort cars by points in descending order
    sort_cars = sorted(v_map.items(), key=lambda x: x[1], reverse=True)
    
    # Take the top 3 cars, or fewer if there are less than 3
    top_3 = sort_cars[:3]
    
    # Sum the points of the top 3 cars
    sum_top_3 = sum(points for c, points in top_3)

    # Prevent division by zero if there are no points
    if sum_top_3 == 0:
        return {"message": "No cars match your criteria."}

    # Calculate the percentage for each car in the top 3
    top_3_map = {
        car: round((points / sum_top_3) * 100, 2)
        for car, points in top_3
    }

    return top_3_map

if __name__ == "__main__":
    app.run(debug=True)