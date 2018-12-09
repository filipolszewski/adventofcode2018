# no plans for reformat here, not happy with part 2 due to a lot of variables,
# but code works for any number of workers, not only 5, and for any set of
# letters

from collections import defaultdict
from itertools import chain

with open("data.txt", 'r') as data:
    pairs = [(x.strip()[5], x.strip()[-12]) for x in data.readlines()]

letters = list(set(chain.from_iterable(pairs)))
letters.sort()
now = set(letters)
after, before = defaultdict(list), defaultdict(list)
answer = list()

for first, second in pairs:
    now.discard(second)
    after[first].append(second)
    before[second].append(first)

while len(now) != 0:
    list_now = list(now)
    list_now.sort()
    next_task = list_now[0]
    answer.append(next_task)
    now.remove(next_task)
    for possible_new in after[next_task]:
        if set(before[possible_new]).issubset(set(answer)):
            now.add(possible_new)

print("Part 1: ", "".join(answer))

# part 2

now = set(letters)
for first, second in pairs:
    now.discard(second)

timeleft = [61 + i for i, _ in enumerate(letters)]
workers_num = 5
finished, finished_set, free, list_now = list(), set(), set(now), list()
answer = 0

while sum(timeleft) != 0:
    # start new tasks if there are workers and free tasks
    list_free = list(free)
    list_free.sort()
    next_task = list_free[
                :min(len(list_free), max(workers_num - len(list_now), 0))]
    free = free.difference(set(next_task))
    list_now.extend(next_task)

    # run tasks until one finishes
    time_step = min([timeleft[letters.index(task)] for task in list_now])
    for now_task in list_now:
        timeleft[letters.index(now_task)] -= time_step
    answer += time_step

    # update list of free tasks
    finished = [task for task in list_now if timeleft[letters.index(task)] == 0]
    list_now = [task for task in list_now if timeleft[letters.index(task)] != 0]
    finished_set.update(finished)
    for finished_task in finished:
        for possible_new in after[finished_task]:
            if set(before[possible_new]).issubset(finished_set) and \
                            possible_new not in finished_set:
                free.add(possible_new)

print("Part 2: ", answer)
