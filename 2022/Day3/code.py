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