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
    if start_x != end_x and start_y != end_y:
        # skip diagonal for now
        print(f' skipped from {start_x},{start_y} to {end_x},{end_y}')
    else:
        print(f'from {start_x},{start_y} to {end_x},{end_y}')
        for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
            if x not in mark:
                mark[x] = {}
            for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
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
aocd.submit(result, part="a", year=2021, day=5)
#exit(0)
