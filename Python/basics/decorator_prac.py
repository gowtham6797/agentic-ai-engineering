def greater_first(func):
    def wrap(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrap

def log_deco(func):
    def wrap(*args):
        print("Values:",args)
        result=func(*args)
        print("result:",result)
        return result
    return wrap

@log_deco
@greater_first
def divide(a,b):
    return a/b

@log_deco
@greater_first
def sub(a,b):
    return a-b

@log_deco
def add(a,b,c):
    return a+b+c

print(divide(2,4))
print(sub(35,15))
print(add(2,5,8))