try:
    with open('cities.txt') as file:
        dict_cities = dict()
        for line in file:
            dict_cities.update({str(line.strip().split(':')[0]):int(line.strip().split(":")[1])})
    print(dict_cities)
    min_value = int(input('Please enter the minimum number of citizens: ')) #1
    for city in dict_cities:
        if dict_cities[city] <= min_value:
            dict_cities.pop(city)
    print(dict_cities)
except:
    print('File doesn\'t exist or there is another problem')

with open('cities.txt') as file:
    dict_cities = dict()
    for line in file:
        dict_cities.update({str(line.strip().split(':')[0]):int(line.strip().split(":")[1])})
print(dict_cities)
min_value = int(input('Please enter the minimum number of citizens: ')) #1

dict_2 = dict()
for city in dict_cities:
    if dict_cities[city] > min_value:
        dict_2.update()
print(dict_cities)