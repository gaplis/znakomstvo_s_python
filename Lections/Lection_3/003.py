def sum(x, y):
    return x+y

sum1 = lambda q, w: q + w

def mylt(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    
calc(sum1, 4, 5)
calc(lambda q, w: q * w, 4, 5)