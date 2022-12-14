import re

filename = 'inputs/day14.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    input_lines = [line.rstrip() for line in f]


def display_map(s_map):

    min_x = min([k[0] for k in s_map]) - 1
    max_x = max(max([k[0] for k in s_map]), 500) + 2  # Make sure source is included
    min_y = min(min([k[1] for k in s_map]), 0) - 1    # Make sure source is included
    max_y = max([k[1] for k in s_map]) + 2

    for this_row in range(min_y, max_y):
        row_print = ''
        for this_col in range(min_x, max_x):
            if (this_col, this_row) not in s_map.keys():
                row_print += '⬛'
            elif s_map[(this_col, this_row)] == '#':
                row_print += '⬜'
            elif s_map[(this_col, this_row)] == 'o':
                row_print += '🟡'
            elif s_map[(this_col, this_row)] == 'x':
                row_print += '❌'
        print(row_print)


def pour_sand(s_map):
    sand_x = 500
    sand_y = 0
    max_y = max([k[1] for k in s_map])
    while True:
        if sand_y > max_y:
            return s_map, False
        elif (sand_x, sand_y + 1) not in s_map:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in s_map:
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in s_map:
            sand_x += 1
            sand_y += 1
        else:
            s_map[(sand_x, sand_y)] = 'o'
            break

    return sand_map, True


def process_input(lines):
    s_map = {(500, 0): 'x'}

    for this_line in lines:
        # Start from the 2nd set and look back at the previous
        x_index = 2
        y_index = 3

        rock_coords = [int(y) for y in re.split(",| -> ", this_line)]
        # [498, 4, 498, 6, 496, 6]

        while y_index < len(rock_coords):
            current_x, current_y = [rock_coords[x_index - 2], rock_coords[y_index - 2]]
            end_x, end_y = [rock_coords[x_index], rock_coords[y_index]]

            x_diff = end_x - current_x
            y_diff = end_y - current_y
            x_inc = y_inc = 0  # By default we increase by zero to avoid div/0 in this if block
            if x_diff:
                x_inc = x_diff//abs(x_diff)  # The direction of change (1 if positive, -1 if negative)
                end_x += x_inc  # Prevents off-by-one error where final coord isn't added
            if y_diff:
                y_inc = y_diff//abs(y_diff)
                end_y += y_inc

            while current_x != end_x or current_y != end_y:
                s_map[(current_x, current_y)] = "#"
                current_x += x_inc
                current_y += y_inc

            x_index += 2
            y_index += 2
    return s_map


sand_map = process_input(input_lines)
keep_going = True
counter = 0
while keep_going:
    sand_map, keep_going = pour_sand(sand_map)
    if keep_going:
        counter += 1
display_map(sand_map)
print(counter)
