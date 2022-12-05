import re
filename = "inputs/2022/day03"


def getPriority(char):
    if char >= 'a' and char <='z':
        return ord(char)-ord('a')+1
    elif char >= 'A' and char <='Z':
        return ord(char)-ord('A')+27
    else:
        return -1

count_1 = 0
count_2 = 0

with open(filename,'r') as file:
    data =file.read()

    lines = data.splitlines()

    for line in lines:
        line_len = len(line)
        pack_len = line_len //2

        x = set(line[:pack_len])
        y = set(line[pack_len:])
        lettre, = x & y 

        #pack =[line[:pack_len], line[pack_len:]]
        #lettre = re.findall(f'[{pack[0]}]',pack[1])
        count_1 +=getPriority(lettre)

    for i in range(0, len(lines), 3):

        x = set(lines[i])
        y = set(lines[i+1])
        z = set(lines[i+2])

        lettre, = x & y & z

        count_2 +=getPriority(lettre)

print(count_1)
print(count_2)