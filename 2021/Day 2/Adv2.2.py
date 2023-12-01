fhd = open('input1.2.txt')

depth = 0
hor = 0
aim = 0
move = dict()
for line in fhd :
    par = line.split()
    dir = par[0]
    dist = int(par[1])
    move[dir] = move.get(dir, 0) + dist
    aim = move.get('down', 0) - move.get('up', 0)
    if dir == 'forward':
        hor += dist
        depth = dist * aim + depth



print(hor*depth)
