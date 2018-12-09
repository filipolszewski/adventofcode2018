first = "abcdefghijklmnoprstqvuwxyzABCDEFGHIJKLMNOPRSTQVUWXYZ"
second = "ABCDEFGHIJKLMNOPRSTQVUWXYZabcdefghijklmnoprstqvuwxyz"
pair_dict = dict(zip(first, second))


def collapse(poly, pairs):
    cnt, i = len(poly), 0
    while i != (len(poly) - 1):
        if pairs[poly[i]] != poly[i + 1]:
            i += 1
        else:
            poly = poly[:i] + poly[i + 2:]
            i -= 1 if i != 0 else 0
            cnt -= 2
    return cnt


with open("data.txt", 'r') as data:
    text = data.readline()
print("Part 1:", collapse(text[:], pair_dict))

min_size = len(text)
for t in "abcdefghijklmnoprstqvuwxyz":
    polymer = text[:]
    polymer = polymer.replace(t, "").replace(pair_dict[t], "")
    size = collapse(polymer, pair_dict)
    if size < min_size:
        min_size = size
print("Part 2:", min_size)
