
fhnd = open('input8.txt')

lines = [line.strip().split(' | ') for line in fhnd.readlines()]

# Creation of Two List with the Decipher Creation Input and Puzzle Output
inp =[line[0].split() for line in lines]
out = [line[1].split() for line in lines]

result = 0
for line in range(len(inp)) :
    trans = dict()
    final = ""

    # Create a translator for each number
    # Starting with Unique Lenghts and...
    for code in inp[line] :
        sortcode = "".join(sorted(code))
        if len(code) == 3 :
            trans['7'] = sortcode
        elif len(code) == 2 :
            trans['1'] = sortcode
        elif len(code) == 4 :
            trans['4'] = sortcode
        elif len(code) == 7 :
            trans['8'] = sortcode

    # using them to decipher first the numbers with six segments...
    for code in inp[line] :
        sortcode = "".join(sorted(code))
        if len(code) == 6:
            if all([number in sorted(code) for number in trans['4']]):
                trans['9'] = sortcode
            elif all([number in sorted(code) for number in trans['7']]) and not all([number in sorted(code) for number in trans['4']]) :
                trans['0'] = sortcode
            else:
                trans['6'] = sortcode

    # and then with length 5 (since I can use '6' segments to find the '5' segments)
    for code in inp[line] :
        sortcode = "".join(sorted(code))
        if len(code) == 5 :
            if all([number in sorted(code) for number in trans['7']]) :
                trans['3'] = sortcode
            elif all([number in sorted(trans['6']) for number in code]) :
                trans['5'] = sortcode
            else :
                trans['2'] = sortcode

    # Use the translator created above to decipher the output
    for output in out[line] :
        sorted_output = "".join(sorted(output))
        for key, value in trans.items() :
            if value == sorted_output :
                final += key

    #Sum Result of Day 8 Part 2 Advent of Code 2021
    result += int(final)

print('Part 2 Result:', result)
