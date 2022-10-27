from re import L


li = [x for x in range(1, 20)]
print(li)

li = list(map(lambda x: x+10, li))
print(li)