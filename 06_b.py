#! /usr/bin/env python3
import aocd
from sys import exit

data = [int(fish) for fish in aocd.get_data(year=2021, day=6).split(',')]

fishes = [0] * (7 + 2)
for fish in data:
    fishes[fish] += 1

print(fishes)
days = 0

last = None
while days < 256:
    for i in reversed(range(len(fishes))):
        tmp = fishes[i]
        fishes[i] = last # all fishes counted down
        last = tmp
    fishes[6] += last # move 0 fishes to next round
    fishes[8] = last # and new fishes
    print(fishes)
    days += 1

result = sum(fishes)
print(f"result = {result}")
aocd.submit(result, part="b", year=2021, day=6)
