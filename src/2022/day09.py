filename = 'inputs/2022/day09'

with open(filename,'r') as file:
	data = file.read().splitlines()

rope_size = 10
rope = [[0,0] for y in range(rope_size)]

head = [0,0]
tail = [0,0]

def set_head_position(head,dir):
	if dir == 'U':
		head[1]+=1
	elif dir == 'D':
		head[1]-=1
	elif dir == 'R':
		head[0]+=1
	elif dir == 'L':
		head[0]-=1

def set_tail_position(tail,head):
	diff_x = head[0] - tail[0]
	diff_y = head[1] - tail[1]
	
	if diff_x > 1 or (diff_x > 0 and abs(diff_y) > 1) :
		tail[0]+=1
	elif diff_x < -1 or (diff_x < 0 and abs(diff_y) > 1):
		tail[0]-=1
	
	if diff_y > 1 or (diff_y > 0 and abs(diff_x) > 1):
		tail[1]+=1
	elif diff_y < -1 or (diff_y < 0 and abs(diff_x) > 1):
		tail[1]-=1

positions = set()

for row in data:
	dir, step = row.split(' ')

	for i in range(int(step)):
		set_head_position(rope[0],dir)
		for k in range(1,len(rope)):
			set_tail_position(rope[k],rope[k-1])
		positions.add(tuple(rope[rope_size-1]))

print(len(positions))