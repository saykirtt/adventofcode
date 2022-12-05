import parse

filename = 'inputs/2015/day06'

def msum(m):
	return sum(sum(m,[]))

def applym(grid,meth,x1,y1,x2,y2):
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            meth(grid,x,y)

def print_grid(g):
	print('\n'.join([''.join([f'{i}'for i in row]) for row in g]))

def on(grid,x,y):
	grid[x][y] = 1

def off(grid,x,y):
	grid[x][y] = 0
def toggle(grid,x,y):
	grid[x][y] = int(not grid[x][y])

command = {
	'turn on':on,
	'turn off':off,
	'toggle':toggle
}


grid_size = 1000
grid = [[0]*grid_size for i in range(grid_size)] 

#turn on 0,0 through 999,999
PATTERN = parse.compile("{action} {x1:d},{y1:d} through {x2:d},{y2:d}")

with open(filename,'r') as file:
	data = file.readlines()

	for line in data:
		match = PATTERN.search(line)
		applym(grid,command[match['action']],match["x1"],match["y1"],match["x2"],match["y2"])

	res = msum(grid)

print(res)
