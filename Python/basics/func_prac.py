def add(a, b):
    """Adds 2 numbers"""
    c = a + b
    return c


a = int(input("Enter the 1st num: "))
b = int(input("Enter the 2st num: "))

a = int(a)
b = int(b)
result = add(a, b)
print("result is", result)
