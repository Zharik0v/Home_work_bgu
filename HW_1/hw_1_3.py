n = input('Введите натуральное число:')
while n.isdigit() != True:
    n = input('Вы ввели не натуральное число!\nВведите натуральное число:')
n = int(n)
while len(str(n)) > 1:
    n = sum([int(i) for i in str(n)])
print(n)