pb_global_b = 12 # global variable

def my_function():
    pb_a = 10 # local variable within function
    print(pb_a)
    print(pb_global_b)
print(pb_a) #  name 'pb_a' is not defined(it is defined inside add indentation)


my_function()