from collections import defaultdict


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

counts = defaultdict(int)

for c in claims:
    for x in c['set']:
        counts[x] += 1

print(sum([val > 1 for val in counts.values()]))

for c in claims:
    result = True
    for x in c['set']:
        if counts[x] != 1:
            result = False
    if result:
        print(c["ID"])
        break
