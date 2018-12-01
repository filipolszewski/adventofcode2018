with open("data.txt") as data:
    shifts = [int(line) for line in data]

history, freq, i = set(), 0, 0
while freq not in history:
    history.add(freq)
    freq += shifts[i % len(shifts)]
    i += 1

print(i, freq)
