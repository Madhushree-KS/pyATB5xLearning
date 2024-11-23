def outer_function():
    var1 = 30
    print("outer1", var1)

    def inner_func1():
        print("func1",var1)
        var2 = 40

        def inner_func2():
            print("func2",var1)
            print("func2",var2)

        inner_func2()

    inner_func1()
outer_function()