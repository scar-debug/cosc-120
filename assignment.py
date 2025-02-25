# Print available options for the user to choose from
print("choose options 1, 2, 3 or 4 ")
print("1.area and circumference of a circle")
print("2.area and perimeter of a triangle")
print("3.area and perimeter of a rectangle")
print("4.area and perimeter of a square")

# Take the user's choice as input and convert it to an integer
choice = int(input("pick among the choices :"))

# Import the math module to use mathematical constants like pi
from math import pi

# Check if the user has chosen option 1 (circle)
if choice == 1:
    # Take input for the radius of the circle
    radius = float(input("Enter radius of the circle"))
    
    # Calculate the area of the circle using the formula: area = π * r^2
    area = float(pi * radius * radius)
    
    # Calculate the circumference of the circle using the formula: circumference = 2 * π * r
    circumference = float(2 * pi * radius)
    
    # Display the area and circumference of the circle
    print(" area of circle ", area)
    print("circumference of circle", circumference)

# Check if the user has chosen option 2 (triangle)
elif choice == 2:
    # Take input for the base and height of the triangle
    base = float(input("Enter base of the triangle"))
    height = float(input("Enter the height of the triangle"))
    
    # Take input for the hypotenuse of the triangle
    hypotenuse = float(input("Enter the hypotenuse of the triangle"))
    
    # Calculate the area of the triangle using the formula: area = 0.5 * base * height
    area = float(0.5 * base * height)
    
    # Calculate the perimeter of the triangle by adding the three sides
    perimeter = (base + hypotenuse + hypotenuse)
    
    # Display the area and perimeter of the triangle
    print("area of triangle", area)
    print("perimeter of triangle", perimeter)

# Check if the user has chosen option 3 (rectangle)
elif choice == 3:
    # Take input for the width and length of the rectangle
    width = float(input("Enter the width of the rectangle"))
    length = float(input("Enter the length of the rectangle"))
    
    # Calculate the area of the rectangle using the formula: area = length * width
    area = float(length * width)
    
    # Calculate the perimeter of the rectangle using the formula: perimeter = 2 * (length + width)
    perimeter = (length + width + length + width)
    
    # Display the area and perimeter of the rectangle
    print("area of rectangle", area)
    print("perimeter of rectangle", perimeter)
#check if user has choosen option 4 (square)
elif choice == 4:
    #Take input for the lenghs
    length = float(input("Enter the length of the square"))
    length = float(input("Enter the length of the square"))
    
    # Calculate the area of the square using the formula: area = 2l
    area = float(length * length)

    # Calculate the perimeter of the square using the formula: perimeter= 2(length + length)
    perimeter = (length + length + length + length)

    # Display the area and perimeter of the square
    print("area of square", area)
    print("perimeter of squqre", perimeter)
    
#check if user has choosen option 4 (square)
    
else:
    print("invalid option choose 1,2,3 or 4")
