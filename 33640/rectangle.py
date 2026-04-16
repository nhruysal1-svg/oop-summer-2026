# Create the Rectangle class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # method: area
    def area(self):
        return self.width * self.height

    # method: perimeter
    def perimeter(self):
        return 2 * (self.width + self.height)


# Create an object
r1 = Rectangle(5, 3)

# Print the area
print(r1.area())

# Print the perimeter
print(r1.perimeter())