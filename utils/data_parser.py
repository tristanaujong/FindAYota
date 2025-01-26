from vehicle_info import Vehicle

def parse_vehicles(car_data):
    car_list = []
    for c in car_data:
        #print(c["model"])
        temp_car = Vehicle(c['id'],c['model'],c['price'],c['body_style'],c['drivetrain'], c['mpg'], c['engine'], c["image_path"])
        car_list.append(temp_car)
    return car_list