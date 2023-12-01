import numpy as np

fhnd = open('input6.txt')

fishes = [int(timer) for timer in fhnd.read().strip().split(',')]

fishes = np.array(fishes, dtype = int)

for day in range(80):
    fishes -= 1
    newlifes = np.count_nonzero(fishes == -1)
    nlarray = np.full((newlifes), 8)
    fishes = np.where(fishes == -1, 6, fishes)
    fishes = np.append(fishes, nlarray)

print(len(fishes))
