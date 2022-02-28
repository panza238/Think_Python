# Creating my first class
import time


class Point(object):
    """Represents point object in 2D
    (This could be generalized for n-D points)"""

    def __init__(self, x=0, y=0, name="Brazilian footballer"):
        """init is the class constructor"""
        self.x = x
        self.y = y
        self.name = name

    def __del__(self):
        """del is the class destructor"""
        print(f"Destroying point {self.name}")

    def print_attributes(self):
        print(f"Coordinates: x={self.x}, y={self.y}")
        print(f"Name: {self.name}")
        print("")


class Rectangle(object):
    """Rectangle in 2D"""

    # This is a way of specifying type. BUT IT IS NOT A TYPE CHECKER!
    def __init__(self, width: int, height: int, low_left_corner_point: Point):
        # I built my own type checker
        if (type(height) is not int) or (type(width) is not int):
            print("width and height MUST be integers")
            del self
            raise TypeError
        self.width = width
        self.height = height
        self.low_left_corner = low_left_corner_point

    def __str__(self):
        """the __str__ method is a  string representation of the object"""
        return f"A Rectangle starting at {self.low_left_corner.name}, with width = {self.width} and height = {self.height}"

    def print_attributes(self):
        print(f"Width: {self.width}, Height: {self.height}")
        print(f"Starts at: {self.low_left_corner.name}")
        print("")

    def __del__(self):
        """One usually does not need destructors!"""
        print(f"Destroying rectangle")


my_point = Point(x=10, y=10, name="Messi")
blank_point = Point()

my_point.print_attributes()
blank_point.print_attributes()
time.sleep(0.5)

# Generating a Rectangle from the one point:
try:
    w, h, p = 100.5, 10, my_point
    print(f"Trying to create a rectangle with parameters {w, h, p}")
    rect1 = Rectangle(width=w, height=h, low_left_corner_point=p)
except Exception as e:
    print("Exception triggered by incorrect typing")
    print(e.__doc__)
    print("")

try:
    w, h, p = 100, 10, my_point
    print(f"Trying to create a rectangle with parameters {w, h, p}")
    rect2 = Rectangle(width=w, height=h, low_left_corner_point=p)
except Exception as e:
    print("Exception triggered by incorrect typing")
    print(e.__doc__)
    print("")

rect2.print_attributes()
# The following line should invoke the __str__ method
print(rect2)

## Shallow Copy vs Deep Copy
import copy
print("\n")
print("Demonstrating shallow and deep copying\n")

rect3 = copy.copy(rect2)
print("same object test")
print("same?", rect2 is rect3)
# This wil yield False. They are not the same object.
# However...
print("corner test")
print("same corner?", rect2.low_left_corner is rect3.low_left_corner)
# This is a shallow copy. Copies the object itself, but not the objects contained in the object...
print("\nDeep Copy\n")
rect4 = copy.deepcopy(rect2)
print("same object test")
print("same?", rect2 is rect4)
# This wil yield False. They are not the same object.
print("corner test")
print("same corner?", rect2.low_left_corner is rect4.low_left_corner)
# Also false!! deepcopy has made a duplicate of every object.

# isinstance
print("isinstance: rect2.start_point, Point", isinstance(rect2.low_left_corner, Point))
print("isinstance: rect2, Point", isinstance(rect2, Point))