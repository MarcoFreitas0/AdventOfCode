import string

ascii_list = list(string.ascii_letters)

with open('input.txt', 'r') as f:
    puzzle_list = f.read().strip().split('\n')

def get_priority(letter):
    return ascii_list.index(letter) + 1

def get_common(bag):
    comp_size = int(len(bag)/2)
    second_comp = bag[comp_size:]

    for letter in bag[:comp_size]:
        if letter in second_comp:
            return get_priority(letter)
        
priority_sum = sum(list(map(get_common, puzzle_list)))

print(f"Answer 1: The total priority is {priority_sum}")

GROUP_SIZE = 3

def get_common_badges(elves):
    elves_content = sorted(elves, key=len)

    for letter in elves_content[0]:
        if letter in elves_content[1] and letter in elves_content[2]:
            return get_priority(letter)

elves_groups = [puzzle_list[i:i+GROUP_SIZE] for i in range(0,len(puzzle_list), GROUP_SIZE)]

priority_sum_2 = sum(list(map(get_common_badges, elves_groups)))

print(f"Answer 2: The total priority is {priority_sum_2}")