#calculating the area and perimeter of a triangle, square and rectangle
#triangle
base=float(input("enter base"))
height=float(input("enter height"))
sideA=float(input("sideA"))
sideB =float(input("sideB"))
area=float(0.5*base*height)
perimeter=float(base+sideA+sideB)
print("area of a triangle",area)
print("perimeter of a triangle",perimeter)
#square
lengthA=float(input("length A"))
lengthB=float(input("length B"))
area=float(lengthA*lengthB)
perimeter=float(2*(lengthA+lengthB))
print("area of a square",area)
print("perimeter of a square",perimeter)
#rectangle
length=float(input("length"))
width=float(input("width"))
area=float(length*width)
perimeter=float(2*(length*width))
print("area of a rectangle",area)
print("perimeter of a rectangle",perimeter)
#python area to calculate the area and circumference of a circle
radius=float(input("enter radius"))
pi=3.142
area= float(pi*radius*radius)
circumference=float(2*pi*radius)
print("area of a circle:",area)
print("circumference of a circle:",circumference)
