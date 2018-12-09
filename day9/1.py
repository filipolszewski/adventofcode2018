from collections import deque

with open("data.txt", 'r') as file:
    data = file.readline().split()
    players, max_marble = int(data[0]), int(data[-2])

circle_deq = deque()
circle_deq.append(0)
scores, min_marble, player = [0] * players, 1, 0

while min_marble <= max_marble:
    if min_marble % 23 != 0:
        circle_deq.rotate(-1)
        circle_deq.append(min_marble)
    else:
        scores[player] += min_marble
        circle_deq.rotate(7)
        scores[player] += circle_deq.pop()
        circle_deq.rotate(-1)
    min_marble += 1
    player = (player + 1) % players

print(max(scores))
