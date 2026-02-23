# Base class
class Vehicle:
    # Method in base class
    def move(self):
        print("The vehicle is moving")
        

# Subclass Car inherits from Vehicle
class Car(Vehicle):
    # Overriding the move() method
    def move(self):
        print("Driving on the road")


# Subclass Bicycle inherits from Vehicle
class Bicycle(Vehicle):
    # Overriding the move() method
    def move(self):
        print("Pedaling on the road")


# Creating objects of subclasses
car = Car()
bicycle = Bicycle()

print("Demonstrating Polymorphism:\n")

# Same method call, different behavior
car.move()        # Calls Car's move()
bicycle.move()    # Calls Bicycle's move()