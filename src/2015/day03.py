import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'inputs/day03')

#grid [[,],]

grid_size = 100


grid = [[0 for x in range(grid_size)]for y in range(grid_size)]


santas = [[0,0],[0,0]]
toggle_santa = False


#location = [0,0]
houses = {tuple(santas[0]),tuple(santas[1])}

with open(filename,'r') as file:
    data = file.read()

    for i,c in enumerate(data):
        match c:
            case '^':
                santas[toggle_santa][0] += 1
            case 'v':
                santas[toggle_santa][0] -= 1
            case '>':
                santas[toggle_santa][1] += 1
            case '<':
                santas[toggle_santa][1] -= 1
        
        houses.add(tuple(santas[toggle_santa]))
        toggle_santa = not toggle_santa

#print(houses)    
print(len(houses))
