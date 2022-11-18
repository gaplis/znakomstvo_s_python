x = 0
y = 0
op = ''

def init(a, b, c):
    global x, op, y
    x = float(a)
    op = b
    y = float(c)

def calculation():
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y
    if op == '/':
        return x / y