import re

filename = 'inputs/2022/day05.txt'
pattern ='move (?P<qty>[0-9]*) from (?P<from>[0-9]*) to (?P<to>[0-9]*)'

with open(filename) as file:
    data = file.read().splitlines()

cargoinfo = []

#getcargoinfo
for row in data:
    if row == '': break
    cargoinfo.append(row[1::4])
cargoinfo.pop()

cargo = [[] for i in range(len(cargoinfo[1]))]
for line in cargoinfo[::-1]:
    for i,crate in enumerate(line):
        if crate != ' ':
            cargo[i].append(crate)

for row in data:
    res = re.match(pattern,row)
    if res:
        qty,fr,to = int(res['qty']),int(res['from'])-1,int(res['to'])-1

        cargo[to] += cargo[fr][-qty:]#[::-1]
        cargo[fr] = cargo[fr][:-qty]

print(''.join([c[-1] for c in cargo]))
