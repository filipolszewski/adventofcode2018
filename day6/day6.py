from collections import defaultdict

with open("data.txt", 'r') as data:
    coords = [(int(x.split(",")[0]), int(x.split(",")[1][1:])) for x in
              data.readlines()]

areas, infinite = defaultdict(int), set()
max_x = max([x[0] for x in coords])
max_y = max([x[1] for x in coords])

for i in range(max_x + 1):
    for j in range(max_y + 1):
        distances = [abs((c[0] - i)) + abs((c[1] - j)) for c in coords]
        closest = coords[distances.index(min(distances))]
        distances.sort()
        if distances[0] != distances[1]:
            areas[closest] += 1
            if i == 0 or i == max_x or j == 0 or j == max_y:
                infinite.add(closest)

print(max([areas[coord] for coord in coords if coord not in infinite]))

region_size = 0
for i in range(max_x + 1):
    for j in range(max_y + 1):
        distances = [abs((c[0] - i)) + abs((c[1] - j)) for c in coords]
        if sum(distances) < 10000:
            region_size += 1
print(region_size)
