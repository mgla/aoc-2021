#! /usr/bin/env python3
import aocd
from math import pow

data = aocd.get_data(year=2021, day=3).splitlines()

bit_count = []
for i in range(len(data[0])):
    bit_count += [0]

for point in data:
    for bit in range(len(bit_count)):
        if point[bit] == "1":
            bit_count[bit] += 1
        else:
            bit_count[bit] -= 1

gamma = 0
epsilon = 0
for bit in range(len(bit_count)):
    if bit_count[bit] > 0:
        gamma += pow(2, len(bit_count) - bit - 1)
    else: # lazy, but maybe it helps for the next puzzle
        epsilon += pow(2, len(bit_count) - bit - 1)

print(f"gamma = {int(gamma)}, epsilon = {int(epsilon)}")
result = int(gamma * epsilon)
aocd.submit(result, part="a", year=2021, day=3)
