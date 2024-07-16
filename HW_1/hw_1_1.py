N = input('Введите натуральное число:')
while N.isdigit() != True:
    N = input('Вы ввели не натуральное число!\nВведите натуральное число:')
N = int(N)
for i in range(0, N):
    print(' ' * (N - i) + '*' * (2 * i + 1))