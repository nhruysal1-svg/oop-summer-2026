# Polymorphism Example

class Car:
    def show(self):
        print("This is a car")


class Plane:
    def show(self):
        print("This is a plane")


objects = [Car(), Plane()]

for obj in objects:
    obj.show()
