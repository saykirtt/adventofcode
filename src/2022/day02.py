import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'inputs/day02')

def get_number(s):
    return ord(s)-64

#déchifre instruction 
def get_sign(sign):
    return chr(ord(sign[0])-23)

def get_score(values):
    turn_score = values[0] - values[1]
    res = 0
    if turn_score == 0: # draw
            res = 3
    elif turn_score == -1 or turn_score == 2: # win
            res = 6
    return res + values[1]

def get_score_2(values):
    res = (values[1]-1)*3
    
    if values[1]==2: #draw
        res += values[0]
    elif  values[1]==3: #win
        sub_res = values[0]+1
        if sub_res > 3:
            sub_res = 1
        res += sub_res
    else:
        sub_res = values[0]-1
        if sub_res == 0:
            sub_res = 3
        res += sub_res   

    return res

score_1 = 0
score_2 = 0

with open(filename,'r') as file:

    for turn in file.readlines():
        
        turn_value = turn.split(' ')        
        turn_value = [get_number(turn_value[0]),get_number(get_sign(turn_value[1]))]
        
       # print(turn_value)

        score_1 += get_score(turn_value) # V1
        score_2 += get_score_2(turn_value) # V2
        #print(score_2)

print(score_1)
print(score_2)

""" better one
def score(p1, p2):
    if (p1 - 1) % 3 == p2:
        return p2 + 1
    elif (p2 - 1) % 3 == p1:
        return p2 + 7
    return p2 + 4


with open("input_files/day02", "r") as f:
    data = f.read().splitlines()
    data = [line.split() for line in data]
    data = [(ord(p1) - ord("A"), ord(p2) - ord("X")) for p1, p2 in data]

moves = [(p1, (p1 + p2 - 1) % 3) for p1, p2 in data]

print(sum(score(p1, p2) for p1, p2 in data))
print(sum(score(p1, p2) for p1, p2 in moves))
"""