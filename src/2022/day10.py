filename = 'inputs/2022/day10'
#filename = 'inputs/datatest'

with open(filename,'r') as file:
	data =file.read().splitlines()

durations = {
	'noop':1,
	'addx':2
}

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
		

print(cycles[179:220])
cycle_no = 20
strength = 0
for signal in cycles[19:220:40]:
	strength += signal * cycle_no
	cycle_no += 40

print(strength)
