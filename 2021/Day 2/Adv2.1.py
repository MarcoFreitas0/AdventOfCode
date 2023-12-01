fhd = open('input1.2.txt')

move = dict()
for line in fhd :
    par = line.split()
    dir = par[0]
    dist = int(par[1])
    move[dir] = move.get(dir, 0) + dist

hor = move['forward']
depth = move['down'] - move['up']

print(hor*depth)
