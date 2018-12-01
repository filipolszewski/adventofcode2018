with open("data.txt") as data:
    print(sum([int(line) for line in data]))
