#! /usr/bin/env python3
import aocd


data = [int(n) for n in aocd.get_data(year=2021, day=1).splitlines()]

print(len(data))

last = -1
increases = -1

for point in data:
    if point > last:
        increases += 1
    last = point

print(increases)
aocd.submit(increases, part="a", year=2021, day=1)
