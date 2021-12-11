#! /usr/bin/env python3

from sys import exit
import aocd

data = [str(n) for n in aocd.get_data(year=2021, day=5).splitlines()]
mark = {}

for line in data:
    (start,end) = line.split(' -> ')
    # check if not diagonal
    start_x, start_y = [int(n) for n in start.split(',')]
    end_x, end_y = [int(n) for n in end.split(',')]
    print(f'from {start_x},{start_y} to {end_x},{end_y}')

    dir_x = 0
    dir_y = 0
    if start_x < end_x:
        dir_x = 1
    elif start_x > end_x:
        dir_x = -1
    if start_y < end_y:
        dir_y = 1
    elif start_y > end_y:
        dir_y = -1

    x = start_x
    y = start_y
    if x not in mark: # lazy but whatevs
        mark[x] = {}
    if y not in mark[x]:
        mark[x][y] = 0
    mark[x][y] += 1
    while x * dir_x < end_x * dir_x or y * dir_y < end_y * dir_y:
        y += dir_y
        x += dir_x
        if x not in mark:
            mark[x] = {}
        if y not in mark[x]:
            mark[x][y] = 0
        mark[x][y] += 1

# find all with more than 1
result = 0
for x in mark.keys():
    for y in mark[x].keys():
        if mark[x][y] > 1:
            result += 1

print(f"result = {result}")
aocd.submit(result, part="b", year=2021, day=5)
