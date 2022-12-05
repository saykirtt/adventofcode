import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'inputs/day01')

floor = 0
first_bas = -1

with open(filename,'r') as file:
    data = file.read()

    for i,c in enumerate(data):
        match c:
            case '(':
                floor += 1
            case ')':
                floor -= 1
        
        if first_bas == -1 and floor < 0 :
            first_bas = i+1

print(floor)
print(first_bas)