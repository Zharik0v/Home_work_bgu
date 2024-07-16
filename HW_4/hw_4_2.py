def gratest(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    else:
        if a > b:
            return gratest(a % b, b)
        else:
            return gratest(a, b % a)
        
    
try:
    print(gratest(int(input('1st number ')), int(input('2nd number: '))))
except:
    print('Input error!')