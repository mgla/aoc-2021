#! /usr/bin/env python3
import aocd

data = [str(n) for n in aocd.get_data(year=2021, day=2).splitlines()]

depth = 0
horizontal = 0
aim = 0

for move in data:
    (direction, amount) = move.split(" ")
    amount = int(amount)
    if direction == "up":
        aim -= amount
    elif direction == "down":
        aim += amount
    elif direction == "forward":
        horizontal += amount
        depth += aim * amount

print(f"depth: {depth}. horizontal: {horizontal}")

result = depth * horizontal
print(f"depth * horizontal: {result}")
aocd.submit(result, part="b", year=2021, day=2)
