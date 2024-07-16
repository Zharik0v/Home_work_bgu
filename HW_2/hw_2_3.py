try:
    with open('input1.txt') as file_1:
        try:
            with open('input2.txt') as file_2:
                with open('output.txt', 'w') as file_3:
                    lines = (file_1.readlines() + file_2.readlines())
                    lst = []
                    for line in lines:
                        line = line.rstrip()
                        lst.append(line)
                    lst = sorted(lst)
                    for word in lst:
                        file_3.write(word + '\n')
        except FileNotFoundError:
            print('File isn\'t found or there was an input error.')
except FileNotFoundError:
    print('File isn\'t found or there was an input error.')