filename = 'inputs/2022/day10'
#filename = 'inputs/test'

with open(filename,'r') as file:
	data =file.read().splitlines()

durations = {
	'noop':1,
	'addx':2
}

def print_2d(m):
	print('\n'.join([''.join([f'{i}'for i in row]) for row in m]))

def draw_pixel(crt,col,row,index):
	if col >= index -1 and col <= index +1 :
		crt[row][col] = "#"


crt_size = (40,6)
crt = [[" " for x in range(crt_size[0])]for y in range(crt_size[1])]

x = 1
cycles =[]
for row in data:
	v = row.split(" ")

	duration = durations[v[0]]
	if v[0] == 'noop':
		inc = 0
	elif v[0] == 'addx':
		inc = int(v[1])

	for i in range(duration):
		cycles.append(x)
		if i == duration -1:
			x += inc
		
#part 1
cycle_no = 20
strength = 0
for signal in cycles[19:220:40]:
	strength += signal * cycle_no
	cycle_no += 40

print(strength)

#part 2
cycle_no = 0
for x,row in enumerate(crt):
	for y,col in enumerate(row):
		draw_pixel(crt,y,x,cycles[cycle_no])
		cycle_no +=1


print_2d(crt)




	

