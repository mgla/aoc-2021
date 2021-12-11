#! /usr/bin/env python3

from sys import exit
import aocd

data = [str(n) for n in aocd.get_data(year=2021, day=4).splitlines()]
rolls = [int(n) for n in data[0].split(',')]

chart_cnt = -1
chart_row_num = 0
charts = {}
chart_lookup = {}
for line in data[1:]:
    if line == '':
        chart_cnt += 1
        chart_row_num = 0
    else:
        if chart_cnt not in charts:
            # initialize new chart
            charts[chart_cnt] = {
                'rows': {},
                'cols': {}
            }
        # read line into current chart
        row_numbers = [int(num) for num in line.split()]
        for col_num in range(len(row_numbers)):
            num = row_numbers[col_num]
            # add to rows for this chart
            if chart_row_num not in charts[chart_cnt]['rows']:
                charts[chart_cnt]['rows'][chart_row_num] = {}
            # add to cols for this chart
            if col_num not in charts[chart_cnt]['cols']:
                charts[chart_cnt]['cols'][col_num] = {}

            charts[chart_cnt]['rows'][chart_row_num][num] = True
            charts[chart_cnt]['cols'][col_num][num] = True
            # finally add chart to loop table
            if num not in chart_lookup:
                chart_lookup[num] = []
            chart_lookup[num] += [chart_cnt]
        chart_row_num += 1

# now that we have the perfect hash map, go over the rolls
for roll in rolls:
    for chart_num in chart_lookup[roll]:
        for col_num in range(len(charts[chart_num]['cols'])):
            if roll in charts[chart_num]['cols'][col_num]:
                del charts[chart_num]['cols'][col_num][roll]
            if roll in charts[chart_num]['rows'][col_num]: # actually row num here
                del charts[chart_num]['rows'][col_num][roll]
            # if either is empty now, we are done here
            if len(charts[chart_num]['rows'][col_num]) == 0:
                print(f"board {chart_num} wins on roll {roll}")
                # calculate score
                print(charts[chart_num])
                result = 0
                for row in charts[chart_num]['rows']:
                    result += sum([n for n in charts[chart_num]['rows'][row].keys()])
                result *= roll
                print(f"result = {result}")
                aocd.submit(result, part="a", year=2021, day=4)
                exit(0)
