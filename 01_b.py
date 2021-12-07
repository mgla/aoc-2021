#! /usr/bin/env python3
import aocd
from collections import deque

data = [int(n) for n in aocd.get_data(year=2021, day=1).splitlines()]

window = deque(data[0:3])
measure = sum(window)
increases = 0

for i in range(3, len(data)):
    window.popleft()
    window.append(data[i])
    newmeasure = sum(window)
    if newmeasure > measure:
        increases += 1
    measure = newmeasure

print(f"# increases: {increases}")
aocd.submit(increases, part="b", year=2021, day=1)
