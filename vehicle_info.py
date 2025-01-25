import json


# class Traits:
#     def __init__(self, engine_type, drive_train, seats, body):
#         self.engine_type = engine_type
#         self.drive_train = drive_train
#         self.seats = seats
#         self.body = body

#     def __str__(self):
#         return (f"Engine Type: {self.engine_type}\n"
#                 f"Drive Train: {self.drive_train}\n"
#                 f"Seats: {self.seats}\n"
#                 f"Body: {self.body}")

class Vehicle:
    def __init__(self, id, model, price, body_style, drivetrain, mpg, engine, image_path):
        self.id = id
        self.model = model
        self.price = price
        self.body_style = body_style
        self.drivetrain = drivetrain
        self.mpg = mpg
        self.engine = engine
        self.image_path = image_path

    def __str__(self):
        return (f"Vehicle: #{self.id}\n"
                f"Model: ${self.model:,.2f}\n"
                f"Price: ${self.price:,.2f}\n"
                f"Body Style: ${self.body_style:,.2f}\n"
                f"Drivetrain: ${self.drivetrain:,.2f}\n"
                f"MPG: ${self.mpg:,.2f}\n"
                f"Engine: ${self.engine:,.2f}\n"
                f"Image Path: ${self.image_path:,.2f}\n")
    
    def get_model(self):
        return self.model

    # @staticmethod
    # def from_json(json_file):
    #     #create a list of vehicle object from the json file
    #     with open(json_file, 'r') as file:
    #         data = json.load(file)

    #     vehicles = []
    #     for entry in data:
    #         id = entry.get('id')
    #         model = entry.get('model')
    #         price = entry.get('price')
    #         mpg = entry.get('mpg')

    #         # extract traits from the json file
    #         traits_data = entry.get('traits', {})
    #         traits = Traits(
    #             engine_type=traits_data.get('engine_type'),
    #             drive_train=traits_data.get('drive_train'),
    #             seats=traits_data.get('seats'),
    #             body=traits_data.get('body')
    #         )

    #         # create a new object for the vehicle
    #         vehicles.append(Vehicle(id, model, price, traits))

    #     return vehicles