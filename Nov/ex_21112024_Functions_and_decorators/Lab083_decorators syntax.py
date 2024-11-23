def decorator1(func):

    def wrapper():
        print("decorator 1")
        func()
    return wrapper


def decorator2(func):
    def wrapper():
        func()
        print("decorator 2")

    return wrapper

@decorator1
@decorator2
def say_hello():
    print("hello")

say_hello()