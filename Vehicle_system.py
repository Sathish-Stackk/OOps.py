#inheritence
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def drive(self):
        print("Car is moving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is moving")

car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()
