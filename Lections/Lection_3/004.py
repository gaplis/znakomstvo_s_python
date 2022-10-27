list0 = []

for i in range(1, 101):
    if(i%2 == 0):
        list0.append(i)

print(list0)

def f(x):
    return x**3

list1 = [i for i in range(1, 21) if i % 2 == 0]
print(list1)

list2 = [(i, i) for i in range(1, 21) if i % 2 == 0]
print(list2)

list3 = [f(i) for i in range(1, 21) if i % 2 == 0]
print(list3)

list4 = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
print(list4)