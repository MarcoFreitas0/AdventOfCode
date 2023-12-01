file = open('input1.1.txt')

numbs = list()
for line in file :
    x = line.strip()
    numbs.append(int(x))

count = 0
prev = None

for numb in numbs :
    if prev is not None and numb > prev :
        count += 1
        print(numb, prev, count)
    prev = numb
