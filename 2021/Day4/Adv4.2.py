import numpy as np

fhnd = open('input4.txt')

lines = [line.split() for line in fhnd]

rnums = [int(num) for num in lines.pop(0)[0].split(',')]

lines.pop(0)

d2ll = tuple()
d3ll = tuple()
for d1arr in lines:
    if len(d1arr) == 0 :
        d3ll += (d2ll,)
        d2ll = tuple()
        continue
    d2ll += (tuple(d1arr),)

d3arr = np.array(d3ll, dtype = int)



found = 0
calnum = tuple()
for numb in rnums :
    if found == len(d3arr) :
        break
    calnum += (int(numb),)
    for d2arr in d3arr :
        if found == len(d3arr) :
            break
        for x in range(5) :
            if np.all(np.in1d(d2arr[:, x], np.array(calnum))) or np.all(np.in1d(d2arr[x, :], np.array(calnum))) :
                lnum = numb
                ncalled = [element for element in d2arr.flat if element not in calnum]
                found += 1
                d2arr[:, :] = -1
                break

print(lnum * sum(ncalled))
