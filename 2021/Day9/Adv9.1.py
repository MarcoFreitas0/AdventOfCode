import numpy as np

fhnd = open('input9.txt')

arrlist = [list(line.strip()) for line in fhnd]

map = np.array(arrlist, dtype = int)

lowers = dict()
for x in range(100) :
    for y in range(100) :
        if x == 0 :
            if y == 0 :
                if map[x, y] < map[x + 1, y] and map[x, y] < map[x, y + 1] :
                    lowers[map[x, y]] = lowers.get(map[x, y], 0) + 1
            elif y == 99 :
                if map[x, y] < map[x + 1, y] and map[x, y] < map[x, y - 1] :
                    lowers[map[x, y]] = lowers.get(map[x, y], 0) + 1
            else :
                if map[x, y] < map[x + 1, y] and map[x, y] < map[x, y + 1] and map[x, y] < map[x, y - 1] :
                    lowers[map[x, y]] = lowers.get(map[x, y], 0) + 1
        elif x == 99 :
            if y == 0 :
                if map[x, y] < map[x, y + 1] and map[x, y] < map[x - 1, y] :
                    lowers[map[x, y]] = lowers.get(map[x, y], 0) + 1
            elif y == 99 :
                if map[x, y] < map[x, y - 1] and map[x, y] < map[x - 1, y] :
                    lowers[map[x, y]] = lowers.get(map[x, y], 0) + 1
            else :
                if map[x, y] < map[x - 1, y] and map[x, y] < map[x, y + 1] and map[x, y] < map[x, y - 1] :
                    lowers[map[x, y]] = lowers.get(map[x, y], 0) + 1
        elif y == 0 :
            if map[x, y] < map[x - 1, y] and map[x, y] < map[x, y + 1] and map[x, y] < map[x + 1, y] :
                lowers[map[x, y]] = lowers.get(map[x, y], 0) + 1
        elif y == 99 :
            if map[x, y] < map[x - 1, y] and map[x, y] < map[x + 1, y] and map[x, y] < map[x, y - 1] :
                lowers[map[x, y]] = lowers.get(map[x, y], 0) + 1
        else :
            if map[x, y] < map[x - 1, y] and map[x, y] < map[x + 1, y] and map[x, y] < map[x, y - 1] and map[x, y] < map[x, y + 1] :
                lowers[map[x, y]] = lowers.get(map[x, y], 0) + 1

result = 0
for key, value in lowers.items():
    result += (key + 1) * value

print(result)
