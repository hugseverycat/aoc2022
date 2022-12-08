filename = 'inputs/day8.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]

tree_map = {}
height = len(lines)
width = len(lines[0])

for y, this_row in enumerate(lines):
    for x, this_col in enumerate(this_row):
        tree_map[(x, y)] = this_col

visible_count = 0
max_scenic = 0

for coord in tree_map:
    cx, cy = coord

    # Detect whether it is on an edge
    if cx in (0, width - 1) or cy in (0, height - 1):
        visible_count += 1  # Edge trees are automatically visible
                            # and have a scenic value of zero
    else:  # We're an inner tree
        right = 0
        right_visible = True
        for x in range(cx+1, width):  # Checking to the right
            if tree_map[coord] <= tree_map[x, cy]:
                right_visible = False
                right += 1
                break
            else:
                right += 1

        left = 0
        left_visible = True
        for x in range(cx-1, -1, -1):  # Checking to the left
            if tree_map[coord] <= tree_map[x, cy]:
                left_visible = False
                left += 1
                break
            else:
                left += 1

        up = 0
        up_visible = True
        for y in range(cy-1, -1, -1):  # Checking to the up
            if tree_map[coord] <= tree_map[cx, y]:
                up_visible = False
                up += 1
                break
            else:
                up += 1

        down = 0
        down_visible = True
        for y in range(cy+1, height):  # Checking to the down
            if tree_map[coord] <= tree_map[cx, y]:
                down_visible = False
                down += 1
                break
            else:
                down += 1

        if up_visible or down_visible or left_visible or right_visible:
            visible_count += 1

        scenic_value = up * down * left * right
        if scenic_value > max_scenic:
            max_scenic = scenic_value

print("Part 1:", visible_count)
print("Part 2:", max_scenic)
