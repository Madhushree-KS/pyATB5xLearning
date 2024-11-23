import time
def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print("start time", start_time)
        func()
        end_time = time.time()
        print("end time", end_time)
        print("time taken to execute all test case", end_time-start_time)

    return wrapper

def print_logs(func):
    def wrapper():
        print("Printing logs started")
        func()
        print("Printing logs ended")

    return wrapper

@time_decorator
@print_logs
def testcase1():
    time.sleep(5)

@time_decorator
def testcase2():
    time.sleep(7)

testcase1()