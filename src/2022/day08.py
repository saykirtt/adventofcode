filename ='inputs/2022/day08'
#filename ='data_test'
with open(filename,'r') as file:
	rows =file.read().splitlines()
cols = list(map(''.join, zip(*rows)))

def get_distance(line,value,sens=1):

	
	count = 1
	for i in range(0,len(line))[::sens]:
		if value <= line[i]:
			return count
		else:
			count +=1

	return len(line)


visible_tree_count = 2*(len(rows)-2 + len(cols))
scores =[]
for x in range(1,len(cols)-1):
	for y in range(1,len(rows)-1):
		value = rows[y][x]
		print(value)
		#part 1
		if max(rows[y][:x]) < value or max(rows[y][x+1:]) < value or max(cols[x][y+1:]) < value or max(cols[x][:y]) < value :
			visible_tree_count +=1

		#part2
		right = get_distance(rows[y][:x],value,-1)
		left = get_distance(rows[y][x+1:],value)
		up = get_distance(cols[x][y+1:],value,-1)
		down = get_distance(cols[x][:y],value)

		scores.append(right*left*up*down)
		break
	break

print(max(scores))
print(visible_tree_count)