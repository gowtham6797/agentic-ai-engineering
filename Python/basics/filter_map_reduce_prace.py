from functools import reduce

nums = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even = list(filter(lambda n: n % 2 == 0, nums))

print("even", even)

# doubles=list(map(lambda n:n*2,even))
doubles = list(map(lambda n: n * 2, list(filter(lambda n: n % 2 == 0, nums))))  # noqa: C417


print("doubles", doubles)

# sum=reduce(lambda a,b:a+b,even)
sum = reduce(lambda a, b: a + b, list(filter(lambda n: n % 2 == 0, nums)))

print("sum", sum)
