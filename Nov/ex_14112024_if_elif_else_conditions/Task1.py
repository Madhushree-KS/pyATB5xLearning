# Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal),
# or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# s1, s2, s3 → int
# o/p →. iso, eq, scalene
a = int(input("enter the input for side a\n"))
b = int(input("enter the input for side b\n"))
c = int(input("enter the input for side c\n"))
if a == b and b == c:
    print("It's a equilateral triangle")
elif a == b or a == c or b == c:
    print("It's a isosceles triangle")
else:
    print("It's a scalene triangle")