def make_claim(s):
    c = dict()
    c['ID'] = int(s[1:s.index("@") - 1])
    c['X'] = int(s[s.index("@") + 2:s.index(",")])
    c['Y'] = int(s[s.index(",") + 1:s.index(":")])
    c['W'] = int(s[s.index(":") + 2:s.index("x")])
    c['H'] = int(s[s.index("x") + 1:])
    c['set'] = set([x + (y * 1000) for x in range(c['X'], c['X'] + c['W'])
                    for y in range(c['Y'], c['Y'] + c['H'])])
    return c


with open("data.txt", 'r') as data:
    claims = [make_claim(row.strip()) for row in data.readlines()]

unique, more, cnt = set(), set(), 0
for c in claims:
    more.update(unique.intersection(c['set']))
    unique = unique.symmetric_difference(c['set'].difference(more))

print("Part 1: ", len(more))

for c in claims:
    if not c['set'].intersection(more):
        print("Part 2: ", c['ID'])




