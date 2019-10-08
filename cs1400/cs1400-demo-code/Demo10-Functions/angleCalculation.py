'''
Requirements Specification: Get three points from the user that create a triangle and
calculate and display the angles of the triangle.

System Analysis:
	pythagorean theorem
    angle formulas
    convert from radians to degrees

System Design:
	1) Ask user for point X1
    2) Ask user for point Y1
    3) Repeat steps 1, 2 for points 2 and 3
    4) Calculate each side of the triangle using pythagorean theorem
    5) Calculate each angle using the angle formulas
    6) Convert angles from radians to degrees
    7) Display the angles

Implementation: Code

Testing:
	1) 	1, 1
    	6.5, 1
        6.5, 2.5
        Result: 15.26, 90.0, 74.74
    2)	30, 20
    	18, 4
        21, 98
        Result: 136.55, 35.04, 8.41
'''

import math

# Get input from user
x1 = float(input("Enter X value for point 1: "))
y1 = float(input("Enter Y value for point 1: "))
x2 = float(input("Enter X value for point 2: "))
y2 = float(input("Enter Y value for point 2: "))
x3 = float(input("Enter X value for point 3: "))
y3 = float(input("Enter Y value for point 3: "))

# Calculate sides
a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

# Calculate angles and convert to degrees
A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

# Display the angles
print("The three angles are ", round(A * 100) / 100.0, round(B * 100) / 100.0, round(C * 100) / 100.0)