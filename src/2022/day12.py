filename = 'inputs/2022/day12'
filename = 'inputs/test'

with open(filename,'r') as file:
	data = file.read()

lines = data.splitlines()
grid = list(map(list, zip(*lines)))

# get S end E position
for x,col in enumerate(grid):
	for y,value in enumerate(col):
		if value == 'E':
			end = (x,y)
			grid[x,y] = 'z'
		elif value == 'S':
			start = (0,x,y)
			grid[x,y] = 'a'


def print_2d(m):
	print('\n'.join([''.join([f'{i}'for i in row]) for row in m]))



# from S go to E


# list avec tout les points attegnable (distance,x,y)
# on pop le point puis on ajoute tout les points atteignable depuis ce point current_distance,x,y

# while (x,y) != end 

edge = [start]

while edge[-1] != end:
	d,x,y = edge.pop()

	for cx,cy in {(x,y-1),(x,y+1),(x+1,y),(x-1,y)}:
			if cx < 0 or cy < 0 or cx > len(grid) or cy > len(col):
				continue
			else:
				edge.append(d+1,cx,cy)


	# ord(a) == ord(b) or ord(a)+1 == ord(b) 


print(start)
print(end)
