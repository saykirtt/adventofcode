filename = 'inputs/2022/day11'
#filename = 'inputs/test'

with open(filename,'r') as file:
	data =file.read()

#get monkey data
monkeys_data = data.split('\n\n')

# monkey data to dict
monkeys = []

for m in monkeys_data:
	rows = m.strip().splitlines()
	monkey = {}

	monkey['items'] = list(map(int,rows[1].split(': ')[1].split(', ')))
	monkey['operation'] = eval("lambda old:"+rows[2].split('=')[1])
	monkey['divisible'] = int(rows[3].split(' ')[-1])
	monkey['true'] = int(rows[4].split(' ')[-1])
	monkey['false'] = int(rows[5].split(' ')[-1])

	monkeys.append(monkey)

monkey_score = [0] * len(monkeys)

#part 1
#round = 20
#part 2
round = 10000

mod = 1 # items over mod of all mod are not useful
for monkey in monkeys:
    mod *= monkey['divisible']


for r in range(round):
	for m_no,m in enumerate(monkeys):
		for i in m['items']:
			#part 1
			#new = m['operation'](i) //3S
			#part 2
			new = m['operation'](i)
			new %= mod

			if new % m['divisible'] == 0:
				monkeys[m['true']]['items'].append(new)
			else:
				monkeys[m['false']]['items'].append(new)

			monkey_score[m_no] += 1

		m['items'] = []
print(monkey_score)
monkey_score.sort()

print(monkey_score[-1]*monkey_score[-2])