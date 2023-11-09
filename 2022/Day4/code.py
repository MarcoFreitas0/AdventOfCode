with open('input.txt') as f:
    text = f.read().strip().split()

#list_values = [[[int(values) for values in pair.split('-')] for pair in line.split(',')] for line in text]
# For better readeability

result = []
for line in text:
    inner_list = []
    pairs = line.split(',')
    for pair in pairs:
        values = pair.split('-')
        inner_list.append([int(value) for value in values])
    result.append(inner_list) 

def check_contains(elves_pair):
    min_sector = min([elves_pair[0][0],elves_pair[1][0]])
    max_sector = max([elves_pair[0][1],elves_pair[1][1]])

    return [min_sector, max_sector] in elves_pair

review_pairs = sum(map(check_contains, result))

print(f"Answer 1: {review_pairs} elves pairs needs reconsideration.")

def check_overlap(elves_pair):
    elve_1 = elves_pair[0]
    elve_2 = elves_pair[1]
    
    return (min(elve_1) <= max(elve_2) and min(elve_2) <= max(elve_1))

review_pairs_2 = sum(map(check_overlap, result))

print(f"Answer 2: {review_pairs_2} elves pairs needs reconsideration.")
