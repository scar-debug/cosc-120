import math

# Function to calculate the area of a circle
def calculate_area(radius):
    return math.pi * radius * radius

# Function to calculate the circumference of a circle
def calculate_circumference(radius):
    return 2 * math.pi * radius
radius = float(input("Enter the radius of the circle: "))

# Calculate the area and circumference
area = calculate_area(radius)
circumference = calculate_circumference(radius)
print(f"The area of the circle with radius {radius} is {area:.2f} square units.")
print(f"The circumference of the circle with radius {radius} is {circumference:.2f} units.")
