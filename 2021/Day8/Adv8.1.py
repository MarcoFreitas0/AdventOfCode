import numpy as np
fhnd = open('input8.txt')

lines = [line.strip().split(' | ') for line in fhnd.readlines()]

output = [line[1].split() for line in lines]

outarr = np.array(output, dtype = str)

counter = 0
for number in outarr.flat:
    if len(number) in (5, 6):
        continue
    counter += 1

print(counter)
