
filename = 'inputs/2022/day12'
#filename = 'inputs/test'

with open(filename,'r') as file:
	data = file.read()

lines = data.splitlines()
grid = [list(x) for x in lines]
# get S end E position


for x,col in enumerate(grid):
	for y,value in enumerate(col):
		if value == 'E':
			end = (x,y)
			grid[x][y] = 'z'
		elif value == 'S':
			start = (x,y)
			grid[x][y] = 'a'

#part 1
start_dist = (0,start[0],start[1])

edge = [start_dist]
vu =[start]
end_ok = False
while edge:
	d,x,y = edge.pop(0)

	value = grid[x][y]
	for cx,cy in {(x+1,y),(x-1,y),(x,y+1),(x,y-1)}:
		if cx < 0 or cy < 0 or cx >= len(grid) or cy >= len(grid[0]):
			continue
		if (cx,cy) in vu:
			continue
		current_value = grid[cx][cy]
		diff = ord(current_value) - ord(value)
		if diff > 1:
			continue

		if (cx,cy) == end:
			print(start,d+1)
			end_ok = True
			break
		vu.append((cx,cy))
		edge.append((d+1,cx,cy))

	if end_ok:
		break

#part 2
start_dist = (0,end[0],end[1])
edge = [start_dist]
vu =[end]
end_ok = False
while edge:
	d,x,y = edge.pop(0)

	value = grid[x][y]
	for cx,cy in {(x+1,y),(x-1,y),(x,y+1),(x,y-1)}:
		if cx < 0 or cy < 0 or cx >= len(grid) or cy >= len(grid[0]):
			continue
		if (cx,cy) in vu:
			continue
		current_value = grid[cx][cy]
		diff = ord(value) - ord(current_value)
		if diff > 1:
			continue

		if current_value == 'a':
			print(d+1)
			end_ok = True
			break
		vu.append((cx,cy))
		edge.append((d+1,cx,cy))

	if end_ok:
		break