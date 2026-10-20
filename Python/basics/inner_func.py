def outer():
    print("outer func")

    def inner(num):
        print("inner func", num)

    return inner


operate = outer()
operate(5)
