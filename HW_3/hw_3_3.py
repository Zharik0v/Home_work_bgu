try:
    with open('cities.txt') as file_1:
        with open('filtered_cities.txt', 'w') as file_2:
            dic = {}
            num = input('Please enter the minimum num of citizens: ')
            while num.isdigit() != True:
                num = input('Please enter the minimum num of citizens: ')
            for line in file_1.readlines():
                names = line.split(':')
                dic[names[0]] = names[1].rstrip()
            sorted_dic = dict(sorted(dic.items()))
            for city in sorted_dic:
                if int(sorted_dic[city]) > int(num):
                    file_2.write(city + ':' + sorted_dic[city] + '\n')
except:
    print('File doesn\'t exist or there is another problem')
