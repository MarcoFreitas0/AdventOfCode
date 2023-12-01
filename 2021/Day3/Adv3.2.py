fhnd = open('input3.txt')

binaries = list()
for line in fhnd :
    binaries.append(line.strip())

o2 = set(binaries)
co2 = set(binaries)

for pos in range(len(binaries[0])) :
    o2count = 0
    co2count = 0
    o2list = list()
    co2list = list()
    for o in o2 :
        o2count = int(o[pos]) + o2count
    for co in co2 :
        co2count = int(co[pos]) + co2count
    o2perc = o2count/len(o2)
    co2perc = co2count/len(co2)
    if o2perc >= 0.5 :
        o2b = '1'
    else :
        o2b = '0'
    if co2perc >= 0.5 :
        co2b = '0'
    else :
        co2b = '1'
    for o in o2 :
        if o[pos] != o2b and len(o2) != 1 :
            o2list.append(o)
    for co in co2 :
        if co[pos] != co2b and len(co2) != 1 :
            co2list.append(co)
    if len(o2list) > 0 :
        o2 = set(o2list)
    if len(co2list) > 0 :
        co2 = set(co2list)

o2 = int(list(o2)[0],2)
co2 = int(list(co2)[0],2)

print(o2*co2)
