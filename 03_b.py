#! /usr/bin/env python3
import aocd

data = aocd.get_data(year=2021, day=3).splitlines()

# test_set = ["011","010","100"]

def rate_set(numbers, bit = None, rate_oxy = True):
    if bit == None:
        bit = 0
    ones = []
    zeroes = []
    for number in numbers:
        if number[bit] == "1":
           ones += [number]
        else:
           zeroes += [number]

    if rate_oxy: # take bigger set, ore ones
        if len(ones) >= len(zeroes):
            keep = ones
        else:
            keep = zeroes
    else: # take smaller set, or zeroes
        if len(ones) < len(zeroes):
            keep = ones
        else:
            keep = zeroes
    if len(keep) == 1:
        return int(keep[0],2)
    else:
        return rate_set(keep, bit + 1, rate_oxy)

oxygen = rate_set(data)
co2 = rate_set(data, rate_oxy = False)
print(f"oxygen: {oxygen}, co2: {co2}, life_support: {co2 * oxygen}")
aocd.submit(co2 * oxygen, part="b", year=2021, day=3)
