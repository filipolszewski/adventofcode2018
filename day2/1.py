from collections import defaultdict

boxes = None
with open("data.txt", 'r') as data:
    boxes = data.readlines()

twos, threes = 0, 0

for box in boxes:
    counts = defaultdict(int)
    for char in box.strip():
        counts[char] += 1

    bool2, bool3 = 0, 0
    for key, value in counts.items():
        if value == 2:
            bool2 = 1
        if value == 3:
            bool3 = 1
    twos += bool2
    threes += bool3

print(twos * threes)
