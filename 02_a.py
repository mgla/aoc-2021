#! /usr/bin/env python3
import aocd

data = [str(n) for n in aocd.get_data(year=2021, day=2).splitlines()]

depth = 0
horizontal = 0

for move in data:
    (direction, amount) = move.split(" ")
    amount = int(amount)
    if direction == "up":
        depth -= amount
    elif direction == "down":
        depth += amount
    elif direction == "forward":
        horizontal += amount

print(f"depth: {depth}. horizontal: {horizontal}")

result = depth * horizontal
print(f"depth * horizontal: {result}")
aocd.submit(result, part="a", year=2021, day=2)
