from collections import defaultdict

with open("data.txt", 'r') as data:
    boxes = [box.strip() for box in data.readlines()]

twos, threes = 0, 0
for box in boxes:
    counts = defaultdict(int)
    for char in box.strip():
        counts[char] += 1

    flag2, flag3 = 0, 0
    for value in counts.values():
        flag2 = True if value == 2 else flag2
        flag3 = True if value == 3 else flag3
    twos += flag2
    threes += flag3

print(twos * threes)
