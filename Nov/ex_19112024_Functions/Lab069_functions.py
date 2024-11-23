# User Defined
# 1.They can't return -> non return
# 2.They can return something
# 3.They have parameters
# 4.They don't have parameters / arguments

# 1. They can't return -> non return
# No Return Type and No Parameter / Argument - NRNP
def greet():
    print("hello")
greet()

# 2. # No Return Type and with Argument/ Param
def greet(name):
    print("hello", name)
greet("madhu")

# 3. No Return Type and with Default Argument ( # positional argument)
def greet(name="Madhu"):
    print("hello", name)
greet()
greet("KS")
print("________________________")

def multiple_args(name="Madhu", age=33, Role="QA"):
    print(name, age, Role)
multiple_args()
multiple_args("nishu")
multiple_args("Avi",37, "lead")

print("________________________")

# 4. Argument + return Type
def sum(a,b):
    return a+b
result = sum(3,4)
print(result)

def sum(a= 5, b=8):
    return a+b
result = sum(4,4)
print(result)

result = sum()
print(result)