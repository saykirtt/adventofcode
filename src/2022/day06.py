filename = 'inputs/2022/day06'

nb_digit = 14 #4 part 1

with open(filename,'r') as file:
	data =file.read()
	for i,c in enumerate(data):
		s = set(data[i:i+nb_digit])
		if len(s) == nb_digit:
			print(i+nb_digit)
			break