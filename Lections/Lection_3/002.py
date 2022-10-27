def calc(x):
    return x+10

print(calc(10))

def calc2(x):
    return x*10

print(calc2(10))

def math(op, x):
    print(op(x))

math(calc2, 10)
math(calc, 10)