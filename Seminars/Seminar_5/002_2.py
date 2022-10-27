lst = [1, 5, 2, 3, 4, 6, 1, 7]
array = []

for i, el1 in enumerate(lst):
    for j, el2 in enumerate(lst[i:]):
        first = el1
        seq = [first] + [first := num for num in lst[j:] if num > first]
        if seq not in array and len(seq) > 1:
            array.append(seq)

print(*array, sep='\n')