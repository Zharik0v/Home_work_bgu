try:
    with open('input.txt') as file:
        course = input('Course name: ')
        student = []
        for line in file.readlines():
            all_students = line.split(':')
            all_courses = all_students[1].strip('\n, ').split(', ')
            if course in all_courses:
                student.append(all_students[0].strip(' '))
        print(student)
except:
    print('File isn\'t found or there was an input error.')