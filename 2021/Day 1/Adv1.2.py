file = open('input1.1.txt')

numbs = list()
for line in file :
    x = line.strip()
    numbs.append(int(x))

count = 0
prev = None
three = list()

for x in range(len(numbs)) :
    if x < 3 :
        continue
    curr = numbs[x-2:x+1]
    prev = numbs[x-3:x]
    s1 = sum(curr)
    s2 = sum(prev)
    if s1 > s2 :
        count += 1
    print(curr, prev, s1, s2, count)
