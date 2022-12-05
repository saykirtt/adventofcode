filename = 'inputs/2022/day04'


count_1 = 0
count_2 = 0
BLANC_SET = set()

with open(filename,'r') as file:
	data =file.read().splitlines()

	for line in data:

		res = [x.split('-') for x in line.split(',')]
		e1 = set(range(int(res[0][0]),int(res[0][1])+1))
		e2 = set(range(int(res[1][0]),int(res[1][1])+1 ))

		e = e1 & e2
		if e == e1 or e == e2:
			count_1 += 1

		if e :
			count_2 +=1

print(count_1)
print(count_2)