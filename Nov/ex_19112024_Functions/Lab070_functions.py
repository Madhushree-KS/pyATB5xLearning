#
# # Create a program to sum of three number from the user input,
# #if user doesn't enter any number', use default as 100, 200, 300
#
num1 = input("enter num 1\n")
num2 = input("enter num 2\n")
num3 = input("enter num 3\n")

def sum(num1=100, num2=200, num3=300):
    return int(num1)+int(num2)+int(num3)

print(sum(num1, num2, num3))
print(sum())
#
# def sum(num1, num2, num3):
#     if not num1:
#         num1 = 100
#     if not num2:
#         num2 = 200
#     if not num3:
#         num3 = 300
#     return int(num1) + int(num2) + int(num3)
#
# print(sum(num1, num2, num3))



