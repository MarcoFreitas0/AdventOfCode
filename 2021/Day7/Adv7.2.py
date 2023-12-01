
fhnd = open('input7.txt')

input = [int(crab) for crab in fhnd.read().strip().split(',')]

prevsum = None
pos = 0
for position in range (max(input) + 1) :
    total = 0
    for crab in input :
        total += abs(crab - position)*(abs(crab - position) + 1) / 2
    if prevsum is None or total < prevsum :
        prevsum = total
        pos = position

print(pos, prevsum)
