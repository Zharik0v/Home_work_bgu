del_ch = input('Please enter characters you want to remove: ') + ';'
try:
    del_ch = input('Please enter characters you want to remove: ') + ';'
    open('output.txt', 'w').close()

    with open('input.txt') as input:
        with open('output.txt', 'a') as output:
            for line in input:
                output.write(f'{line.rstrip().rstrip(del_ch)[::-1]}\n')

except:
    print('File isn\'t found or there was an input error.')