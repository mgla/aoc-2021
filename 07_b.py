#! /usr/bin/env python3
import aocd
from sys import exit

crabs = [int(crab) for crab in aocd.get_data(year=2021, day=7).split(',')]
costs = [0] * max(crabs) # 0 is in my input, so this is safe

for crab in crabs:
    for pos in range(len(costs)):
        diff = abs(pos - crab)
        costs[pos] += (diff * diff + diff)/2

# find minimum item
min = costs[0]
for pos in range(len(costs)):
    if costs[pos] < min:
        min = costs[pos]

result = int(min)
print(f"result = {result}")
aocd.submit(result, part="b", year=2021, day=7)
