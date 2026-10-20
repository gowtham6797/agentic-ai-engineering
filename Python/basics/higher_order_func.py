def square(num):
    return num * num


def cube(num):
    return num * num * num


def operate(nums, operation):
    for i in nums:
        res = operation(i)
        print(res)


operate([3, 4, 5], square)
