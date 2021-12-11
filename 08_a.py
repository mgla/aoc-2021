#! /usr/bin/env python3
import aocd
from sys import exit

data = [str(n) for n in aocd.get_data(year=2021, day=8).splitlines()]
codes = []
outputs = []
for line in data:
    (code, output) = line.split(' | ')
    codes += [[str(n) for n in code.split()]]
    outputs += [[str(n) for n in output.split()]]

result = 0
for output in outputs:
    for number in output:
        print(number)
        if len(number) in [2, 4, 3, 7]:
            result += 1

print(f"result = {result}")
aocd.submit(result, part="a", year=2021, day=8)
