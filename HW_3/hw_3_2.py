try:
    with open('input.txt') as file_1:
        with open('output.txt', 'w') as file_2:
            all_products = {}
            for line in file_1.readlines():
                if ':' in line:
                    names = line.split(':')
                    if any(char.isdigit() for char in names[1]):
                        names[0] = names[0].strip('" ')
                        names[1] = names[1].strip('\n, ')
                        if names[0] in all_products:
                            all_products[names[0]] += int(names[1])
                        else:
                            all_products[names[0]] = int(names[1])
            for product in all_products:
                file_2.write(product + ': ' + str(all_products[product]) + '\n')
except:
    print('File isn\'t found or there was an input error.')