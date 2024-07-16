def is_balanced(line):
    if len(line) == 0:
        return True
    elif '()' in line or '<>' in line or '{}' in line or '[]' in line:
        return is_balanced(line.replace('()', '').replace('<>', '').replace('{}', '').replace('[]', ''))
    else:
        return False

try:
    with open('input.txt') as file:
        lines = [line.strip() for line in file ]
        for line in lines:
                line = ''.join(i for i in line if i in '({<[]>})')
                with open('output.txt', 'w') as file_out:
                    file_out.write(f'{is_balanced(line)}\n')
except:
    print('File isn\'t found or there was an input error.')

