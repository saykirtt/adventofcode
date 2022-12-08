current_dir = root = {}
path = []

filename = 'inputs/2022/day07.txt'

with open(filename) as file:
    data = file.read().splitlines()

# make dict from command
for line in data:
    args = line.split(' ')

    if args[0] == '$': # commande
        if args[1] == 'cd':
            dir = args[2]
            if dir == "..":
                current_dir = path.pop()
            elif dir == "/":
                current_dir = root
                path = []
            else:
                if dir not in current_dir:
                    current_dir[dir] = {}
                path.append(current_dir)
                current_dir = current_dir[dir]

    else: #dir or file
        arg,name = args[0],args[1]
        if arg =="dir":
            
            if name not in current_dir:
                current_dir[name] = {}
        else:
            current_dir[name] = int(arg)

# get all_size of dir > 100000
def part1(dir = root):
    
    if type(dir) == int:
        return (dir,0)

    size = 0
    all_size = 0

    for child in dir.values():
        s,a = part1(child)
        size += s
        all_size += a
    
    if size <= 100000:
        all_size += size
    return (size, all_size)

print(part1()[1])

def size(dir = root):
    if type(dir) == int:
        return dir
    return sum(map(size, dir.values()))

target = size() - (7-3)*1000000

def part2(dir = root):
    all_size = float("inf")
    if size(dir) >= target:
        all_size = size(dir)
    for child in dir.values():
        if type(child) == int:
            continue
        q = part2(child)
        all_size = min(all_size, q)
    return all_size

print(part2())
