filename = 'inputs/2022/day11'
filename = 'inputs/test'

with open(filename,'r') as file:
	data =file.read()

#get monkey data
monkeys_data = data.split('\n\n')

# monkey data to dict
monkeys = []

for m in monkeys_data:
	rows = m.strip().splitlines()
	monkey = {}
	for r in rows:
		key,value = r.split(':')
		monkey[key.replace(" ","")]= value[1:].split(' ')

	monkey['items'] = [int(i.replace(',','')) for i in monkey['Startingitems']]
	monkeys.append(monkey)

#print(monkeys)

# dividible => a % b == 0

def ceil(n):
    return int(-1 * n // 1 * -1)

def multiply(a,b):
	#return ceil((a/10) * (b/10) *100)
	return a * b 

def addition(a,b):
	return a+b

sign = {
	'*':multiply,
	'+':addition
}

monkey_score = [0 for i in range(len(monkeys))]

round = 20 #10000

for r in range(round):
	for m_no,m in enumerate(monkeys):
		fct = sign[m['Operation'][3]]
		value = m['Operation'][4]

		divisible = int(m['Test'][2])

		indexs = (int(m['Iftrue'][3]),int(m['Iffalse'][3]))

		for i in m['items']:
			b = i if value == 'old' else int(value)
			new = fct(i,b) // 3
			
			if new % divisible == 0:
				index = indexs[0]
			else:
				index = indexs[1]

			monkeys[index]['items'].append(new)
			monkey_score[m_no] += 1

		m['items'] = []
print(monkey_score)
monkey_score.sort()

print(monkey_score[-1]*monkey_score[-2])

