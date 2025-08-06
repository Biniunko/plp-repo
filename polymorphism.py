class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden in subclasses")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚲"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

vehicles = [Car(), Plane(), Bicycle(), Boat()]


for v in vehicles:
    print(f"{v.__class__.__name__} is: {v.move()}")
