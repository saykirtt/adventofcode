filename ='inputs/day05'
import re
#containe voyel 'aeiou'
# containe 2 lettres twins
# not container 'ab' 'cd','pq','xy'

count_1 = 0
count_2 = 0
with open(filename,'r') as file:
    for line in file.readlines():
        nb_voyel = len(re.findall('[aeiou]',line))
        nb_twin = len(re.findall(r'(.)\1',line))
        nb_forbiden = len(re.findall('ab|cd|pq|xy',line))

        nb_twice_2_lettre = len(re.findall(r'(.{2}).*\1',line))
        nb_seperate_twin = len(re.findall(r'(.).\1',line))

        count_1 += nb_voyel > 2 and nb_twin > 0 and nb_forbiden == 0
        count_2 += nb_seperate_twin > 0 and nb_twice_2_lettre > 0

print(count_1)
print(count_2)