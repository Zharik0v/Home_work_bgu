from statistics import mean

grades = dict()
try:
    with open('input.txt') as input:
        for line in input:
            line = line.strip().split(',')
            line = [i.strip() for i in line]
            for i in line:
                grades[line[0]] = int(line[1])
    mean_val = mean([int(i) for i in grades.values()])

    open('output.txt', 'w').close()
    for i in grades.keys():
        if grades[i] > mean_val:
            with open('output.txt', 'a') as output:
                output.write(f'{i}\n')
except:
    print('File isn\'t found or it\'s not correct.')