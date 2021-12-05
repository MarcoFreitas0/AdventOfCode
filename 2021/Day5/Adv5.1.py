import numpy as np

fhnd = open('input5.txt')

map = np.zeros((1000,1000), dtype = int)

def draw (coordinate) :
    x1, y1, x2, y2 = coordinate
    if y1 == y2 :
        if x1 > x2:
            x1, x2 = x2, x1
        map[x1:x2, y1] = np.where(True, map[x1:x2, y1] + 1, 0)
    elif x1 == x2 :
        if y1 > y2:
            y1, y2 = y2, y1
        map[x1, y1:y2] = np.where(True, map[x1, y1:y2] + 1, 0)

gas = tuple()
for line in fhnd :
    coords= tuple()
    ll = line.strip().split(' -> ')
    for lic in ll :
        coord = lic.split(',')
        coordi = tuple([int(x) for x in coord])
        coords += coordi
    gas += (coords,)

for coord in gas :
    draw(coord)

print(np.count_nonzero(map >= 2))
