fhnd = open('input3.txt')

binaries = list()
for line in fhnd :
    binaries.append(line.strip())

gamma = ''
epsilon = ''

for pos in range(len(binaries[0])) :
    count = 0
    for binary in binaries :
        count = int(binary[pos]) + count
    perc = count/len(binaries)
    if perc > 0.5 :
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else :
        gamma = gamma + '0'
        epsilon = epsilon + '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)
