import os
import hashlib

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'inputs/day04')

nb_zero = 6

target_hash = b'0'*nb_zero


with open(filename,'r') as file:
    data = file.read()

hash = b''
i = 0
while target_hash != hash[:nb_zero]:
    i += 1
    hash = hashlib.md5((data+str(i)).encode()).hexdigest().encode()

print(hash)
print(i)