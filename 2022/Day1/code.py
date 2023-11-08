file_path = 'input.txt'

with open(file_path, 'r') as f:
    text = f.read()

elfs = text.split('\n\n')

elfs = list(map(lambda x: x.split('\n'), elfs))

cal = []
for elf in elfs:
    cal.append(sum([int(calories) for calories in elf if calories != '']))

cal.sort(reverse=True)

print(f"Answer 1: Max Calories is {max(cal)}")
print(f"Answer 2: Sum of top 3 Calories is {sum(cal[:3])}")