# unrefactored, no time for this unfortunately.

import datetime
from collections import defaultdict


def make_info_row(row):
    r = dict()
    r['datetime'] = datetime.datetime.\
        strptime(row.split("]")[0][1:], '%Y-%m-%d %H:%M')
    r['shift'] = "begins" in row.split("]")[1]
    r['gid'] = row.split("]")[1].strip().split()[1][1:] if r['shift'] else None
    r['falls'] = "falls" in row.split("]")[1]
    r['wakes'] = "wakes" in row.split("]")[1]
    return r


with open("data.txt", 'r') as data:
    info = [make_info_row(box.strip()) for box in data.readlines()]
info.sort(key=lambda x: x['datetime'])

counts_per_guard = defaultdict(lambda: [0] * 60)
sum_for_guard = defaultdict(int)

id, max_sum, max_sum_gid = 0, 0, None
sleep_start, sleep_end = 0, 0
for entry in info:
    if entry['gid'] is not None:
        id = entry['gid']
    if entry['falls']:
        sleep_start = entry['datetime'].minute
    if entry['wakes']:
        sleep_end = entry['datetime'].minute
        for i in range(sleep_start, sleep_end):
            counts_per_guard[id][i] += 1
        sum_for_guard[id] += (sleep_end - sleep_start)
        if sum_for_guard[id] > max_sum:
            max_sum = sum_for_guard[id]
            max_sum_gid = id

best = counts_per_guard[max_sum_gid]
minute = best.index(max(best))
print(minute * int(max_sum_gid))

# part 2

best_id, max_count = None, 0
for id, counts in counts_per_guard.items():
    max_for_g = max(counts)
    if max_for_g > max_count:
        max_count = max_for_g
        best_id = id


best = counts_per_guard[best_id]
minute = best.index(max(best))
print(minute * int(best_id))
