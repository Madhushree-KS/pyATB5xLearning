def add_before_and_after_testcase(func):

    def wrapper():
        print("Before running the testcase")
        print("start browser")
        func()
        print("Close the browser")
    return wrapper()

@add_before_and_after_testcase
def testcase():
    print("UI changes verified")
