# Write a Python program to calculate the
# area of a circle given its radius using the formula
# ``` area=π×r^2``` ( Take pie as 3.14)

r = float(input("enter the radius\n"))
Area = 3.1423141*r**2
print(Area)

print("Area of the circle is -> ", Area)

print(f"Area of the circle is -> :  {Area:.2f}")

#* -> mul
#** -> power
import math
radius = float(input("enter the radius of the circle\n"))
print(math.pi)
print(math.pow(radius,2))
area = math.pi * math.pow(radius, 2)
print("Area of the circle is -> ", area)

# print(3.14 * (float(input("Enter the radius of the circle\n"))**2))




