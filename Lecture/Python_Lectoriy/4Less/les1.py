# def f(x):
#     return x*x

# print(f(5))
# print(type(f))

'''
def calc1(a, b):
    return a+b

def calc2(a, b):
    return a*b

def math(op, x, y):
    print(op(x, y))

math(calc1, 5, 2)#calc = op


def math(op, x, y):
    print(op(x, y))

calcc1 = lambda a,b: a+b

math(calcc1, 5, 45)
'''


def calc2(a, b):
    return a*b

def math(op, x, y):
    print(op(x, y))

math(lambda a,b: a+b, 5, 45)