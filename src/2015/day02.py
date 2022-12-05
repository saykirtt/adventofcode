import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'inputs/day02')

#l,w,h

paper = 0
ribbon = 0

with open(filename,'r') as file:

    for present in file.readlines():
        sizes = [int(x) for x in present.split("x")]
        sizes.sort()

        paper += 3 * sizes[0]*sizes[1] + 2 * sizes[2]*sizes[1] + 2 * sizes[0]*sizes[2] 
        ribbon += sizes[0]*2 +sizes[1]*2+ sizes[0]*sizes[1]*sizes[2]
print(paper)
print(ribbon)