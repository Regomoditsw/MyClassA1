# MyClassA1

smart phone


class Smartphone:
    def __init__(self, brand, model, battery_life, storage):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours
        self.storage = storage  # in GB

    def make_call(self, number):
        print(f"Calling {number}...")

    def take_picture(self):
        print(f"Taking a picture with {self.model} camera!")

    def charge(self, hours):
        self.battery_life += hours
        print(f"Charging for {hours} hours. Battery life is now {self.battery_life} hours.")

    def display_info(self):
        print(f"Smartphone Info: {self.brand} {self.model} with {self.storage}GB storage and {self.battery_life} hours of battery life.")

#  Usage:
iphone = Smartphone("Apple", "iPhone 13", 20, 128)
iphone.display_info()
iphone.make_call("1234567890")
iphone.charge(3)
iphone.take_picture()


## polymorphism 

class Vehicle:
    def move(self):
        pass  # Placeholder for polymorphic behavior

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Usage:
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
