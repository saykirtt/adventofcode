filename = 'inputs/2022/day13'
#filename = 'inputs/test'

with open(filename,'r') as file:
	data =file.read()

def compare(a,b):
	if type(a)== int:
		if type(b)==int:
			return a - b
		else:
			return compare([a],b)
	else:
		if type(b)==int:
			return compare(a,[b])
		else:
			for x, y in zip(a, b):
				v = compare(x, y)
				if v:
					return v
			return len(a) - len(b)

def bSort(arr):
	n = len(arr)

	for i in range(n):
		for j in range(0, n-i-1):
			if compare(arr[j],arr[j+1]) > 0: 
				arr[j], arr[j+1] = arr[j+1], arr[j]

#part 1
""""
packs = data.split('\n\n')

with open('res2','w') as w:
	sum = 0
	for i,pack in enumerate(packs): #[46:47]
		l,r = map(eval,pack.split('\n'))
		res =compare(l,r)
		if res < 0:
			sum += i+1
			w.write(f'{i}\n')
	print('=')
	print(sum)
"""
#part 2 
packs = list(map(eval,data.replace('\n\n','\n').splitlines()))
packs.append([[2]])
packs.append([[6]])


bSort(packs)
start = packs.index([[2]])+1
end = packs.index([[6]]) +1

print(start*end)