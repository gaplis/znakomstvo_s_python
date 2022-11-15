# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# 1+2*3 => 7;
# (1+2)*3 => 9;

# С помощью рекурсии может работать даже с внутренними скобками, единственное недоработано, если бы числа были двузначными
# или если бы скобки были не внутренними, а соседними, к примеру (2+2)*(3+3), но так тут можно вообще кучу вчего доработать,
# о чем даже не просили и что займет немало времени, поэтому оставлю на будущее)

def calc(ex):
    while len(ex) != 1:
        res = 0
        if "(" in ex:
            recursion_list = []
            for first in range(len(ex)):
                if ex[first] == '(':
                    first_bracket = first
                    break
            for second in range(len(ex)-1, 0, -1):
                if ex[second] == ')':
                    second_bracket = second
                    break
            for item in range(first_bracket + 1, second_bracket):
                recursion_list.append(ex[item])
            ex[first] = calc(recursion_list)
            for del_item in range(second_bracket, first_bracket, -1):
                ex.pop(del_item)
        for i in range(len(ex)):
            if '*' in ex or '/' in ex:
                if ex[i] == '*':
                    res = int(ex[i-1]) * int(ex[i+1])
                    break
                elif ex[i] == '/': 
                    res = int(ex[i-1]) / int(ex[i+1])
                    break
            elif ex[i] == '+':
                res = int(ex[i-1]) + int(ex[i+1])
                break
            elif ex[i] == '-':
                res = int(ex[i-1]) + int(ex[i+1])
                break
        ex[i] = res
        ex.pop(i+1)
        ex.pop(i-1)
    result = ex[0]
    return result

input_data = input('Введите арифметическое выражение: ')

# Если пользователь будет вводить, к примеру, так ((2 + 2) + 3) / 2, а не так ((2+2)+3)/2, то получится список с частами-пробелами, 
# а моя программа завязана на том, что в итоговом списке не будет ничего, кроме числел и операций, поэтому последующее выражение 
# необходимо в данном случае, чтобы эти пробелы убрать из строки)

if ' ' in input_data:
    input_data = input_data.replace(' ', '')

arithmetic_expression = [let for let in input_data]

# Мои попытки решить, как сделать двузначные числа)
# for num in range(len(arithmetic_expression)):
#     if arithmetic_expression[num] == int(arithmetic_expression[num]) and arithmetic_expression[num+1] == int(arithmetic_expression[num+1]):
#         arithmetic_expression[num] = str(arithmetic_expression[num]) + str(arithmetic_expression[num+1])
#         arithmetic_expression.pop(num+1)

print(f'{input_data}={calc(arithmetic_expression)}')