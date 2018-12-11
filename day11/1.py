from collections import defaultdict


def hundreds(num):
    return int(str(num)[-3:-2]) if num > 99 else 0


def calc_square(serial, s, x, y, powers):
    if s == 1:
        return hundreds((x + 10) * (((x + 10) * y) + serial)) - 5
    if s % 2 == 0:
        return powers[(x, y, s / 2)] + \
               powers[(x + s / 2, y, s / 2)] + \
               powers[(x, y + s / 2, s / 2)] + \
               powers[(x + s / 2, y + s / 2, s / 2)]
    else:
        power = powers[(x, y, s - 2)]
        power += sum([powers[(X, y + s - 1, 1)] for X in range(x, x + s)])
        power += sum([powers[(x + s - 1, Y, 1)] for Y in range(y, y + s - 1)])
        return power


with open("data.txt", 'r') as file:
    serial_number = int(file.readlines()[0])

known_powers = defaultdict(int)
max_power, best = 0, (1, 1, 1)

for size in range(1, 300):
    for i in range(1, 302 - size):
        for j in range(1, 302 - size):
            square_power = calc_square(serial_number, size, i, j, known_powers)
            known_powers[(i, j, size)] = square_power

            if square_power > max_power:
                max_power = square_power
                best = (i, j, size)

print(best)
