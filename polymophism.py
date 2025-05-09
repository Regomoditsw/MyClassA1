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

# Example Usage:
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()  # This will call the move method of each subclass
