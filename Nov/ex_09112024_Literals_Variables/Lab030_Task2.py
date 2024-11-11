# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

num1 = int(input("enter number 1\n"))
num2 = int(input("enter number 2\n"))

quotient = num1//num2
reminder = num1%num2

print("quotient is", quotient)
print("remainder is",reminder)