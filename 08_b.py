#! /usr/bin/env python3
import aocd
from sys import exit

test_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

data = [str(n) for n in aocd.get_data(year=2021, day=8).splitlines()]
#data = [str(n) for n in test_data.splitlines()]
displays = []
print(data[0])
for line in data:
    (code, output) = line.split(' | ')
    key = [str(n) for n in code.split()]
    to_solve = [str(n) for n in output.split()]
    displays.append([key, to_solve])


result = 0
for display in displays: # FIXME only solve first one
    solution = {}
    puzzle = map(lambda x: ''.join(sorted(x)), display[1])
    to_solve = dict(map(lambda x: (''.join(sorted(x)), True), display[1]))
    print('code', display[0])
    print('puzzle', display[1])
    tries = 0
    while len (display[0]) > 0 and len(to_solve) > 0 and tries < 10:  # assume every puzzle is solvable:w
        tries+= 1
        for index, number in enumerate(display[0]):
            key = "".join(sorted(number))
            if key in solution:
                display[0].pop(index)
                if key in to_solve:
                    del to_solve[key]
            else:
                unique_key = {
                    2: 1,
                    3: 7,
                    4: 4,
                    7: 8
                }
                if len(key) in unique_key:
                    solution[key] = unique_key[len(key)]
                # special solutions here
                if len(key) == 5: # can be 2, 3 or 5
                    # if we know 7 or 1, we can identify 3
                    if 7 in solution.values():
                        key_7 = [k for k, v in solution.items() if v == 7][0]
                        if all([char in key for char in key_7]): # 0 or 9
                            solution[key] = 3
                        else: # 2 or 5
                            if 6 in solution.values():
                                key_6 = [k for k, v in solution.items() if v == 6][0]
                                if all([char in key_6 for char in key]): # 0 or 9
                                    solution[key] = 5
                                else: # 2 or 5
                                    solution[key] = 2
                            else:
                                pass # implement me or wait?
                    elif 1 in solution.values():
                        key_1 = [k for k, v in solution.items() if v == 1][0]
                        if all([char in key for char in key_1]): # 0 or 9
                            solution[key] = 3
                        else: # 2 or 5
                            if 6 in solution.values():
                                key_6 = [k for k, v in solution.items() if v == 6][0]
                                if all([char in key_6 for char in key]): # 0 or 9
                                    solution[key] = 5
                                else: # 2 or 5
                                    solution[key] = 2
                            else:
                                pass # implement me or wait?
                    else:
                        pass # implement me or wait?

                if len(key) == 6: # can be 0, 6 or 9
                    # if we found 7, if not all 7 characters are in this, it is 6
                    is_6 = True
                    if 7 in solution.values():
                        key_7 = [k for k, v in solution.items() if v == 7][0]
                        if all([char in key for char in key_7]): # 0 or 9
                            # if we found 4, we can check if it is fully in key
                            # if yes, key means 9
                            if 4 in solution.values():
                                key_4 = [k for k, v in solution.items() if v == 4][0]
                                if all([char in key for char in key_4]): # 0 or 9
                                    solution[key] = 9
                                else:
                                    solution[key] = 0
                            else:
                                pass # implement me or wait?
                        else: # 6
                            solution[key] = 6
    if len(to_solve) == 0:
        solution = int(''.join([str(solution[key]) for key in puzzle]))
        result += solution
        print(f'SOLVED: {solution}')
    else:
        print(f'try# {tries}')
        print(f'to_solve: {to_solve.keys()}')
        print(f'solution: {solution}')
        print(f'display 0: {display[0]}')
        print('failed to solve')
        exit(10)

print(f"result = {result}")
aocd.submit(result, part="b", year=2021, day=8)
