import numpy as np

fhnd = open('input5.txt')

map = np.zeros((1000,1000), dtype = int)

def draw (coordinate) :
    x1, y1, x2, y2 = coordinate
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1
    if y1 == y2 :
        map[x1:x2 + 1, y1] =  map[x1:x2 + 1, y1] + 1
    elif x1 == x2 :
        if y1 > y2:
            y1, y2 = y2, y1
        map[x1, y1:y2 + 1] = map[x1, y1:y2 + 1] + 1
    else :
        while True:
            if x1 == x2 + 1:
                break
            map[x1, y1] += 1
            if y1 > y2:
                y1 -= 1
            else :
                y1 += 1
            x1 += 1

pipes = tuple()
for line in fhnd :
    pipe= tuple()
    almost = line.strip().split(' -> ')
    for lic in almost :
        coord = lic.split(',')
        coords = tuple([int(x) for x in coord])
        pipe += coords
    pipes += (pipe,)

for pipe in pipes :
    draw(pipe)

print('Part 2 Result:', np.count_nonzero(map >= 2))

