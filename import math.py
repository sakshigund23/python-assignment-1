import math

# Area of Circle
def circle_area(radius):
    return math.pi * radius * radius

# Area of Rectangle
def rectangle_area(length, width):
    return length * width

# Area of Triangle
def triangle_area(base, height):
    return 0.5 * base * height


# Example usage
print("Area of Circle:", circle_area(5))
print("Area of Rectangle:", rectangle_area(10, 4))
print("Area of Triangle:", triangle_area(6, 8))