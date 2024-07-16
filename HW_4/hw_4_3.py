def num_of_ways(n):
    if n == 0 or n == 1 or n == 2:
        return n
    else:
        return num_of_ways(n - 1) + num_of_ways(n - 2)
    

try:
    print(num_of_ways(int(input('Please, enter number of stairs: '))))
except:
    print('Input error!')