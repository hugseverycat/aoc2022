filename = 'inputs/day8.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]

tree_map = {}
HEIGHT = len(lines)
WIDTH = len(lines[0])

# Store each tree in the tree_map dictionary where the (x,y) location is the
# key and the value is the tree height.
for y, this_row in enumerate(lines):
    for x, this_col in enumerate(this_row):
        tree_map[(x, y)] = this_col

visible_count = 0
max_scenic = 0


def get_visibility(start_tree, t_map, step_directions):
    # How much we will increment x and y. Should be 1, 0, or -1
    step_x, step_y = step_directions
    # Set current_x and current_y to the first neighbor
    current_x, current_y = start_tree[0] + step_x, start_tree[1] + step_y
    visible_trees = 0
    is_visible = True

    # We will move from the current tree towards the edge
    while current_x in range(0, WIDTH) and current_y in range(0, HEIGHT):
        # If we encounter a tree that is higher than our start tree
        if t_map[start_tree] <= t_map[current_x, current_y]:
            is_visible = False  # start_tree is not visible from this side
            visible_trees += 1  # We can see the tree that blocks us
            break  # Stop looping; we've been blocked
        else:
            visible_trees += 1  # We can see a tree that is shorter :)
        # Next tree, please!
        current_x += step_x
        current_y += step_y
    return is_visible, visible_trees


# Iterate through each tree in the dictionary.
for coord in tree_map:
    cx, cy = coord

    # If the tree is on an edge, it is visible and has no scenic value.
    if cx in (0, WIDTH - 1) or cy in (0, HEIGHT - 1):
        visible_count += 1

    # If this is an inner tree, call the get_visibility function to see
    # if the tree is visible and how many trees are visible from this tree
    else:
        # The (1, 0) etc tuple at the end is which direction we'll check
        # from the tree. For example (1, 0) will increase x so we're checking
        # towards the right edge.
        right_visible, right = get_visibility(coord, tree_map, (1, 0))
        left_visible, left = get_visibility(coord, tree_map, (-1, 0))
        up_visible, up = get_visibility(coord, tree_map, (0, -1))
        down_visible, down = get_visibility(coord, tree_map, (0, 1))

        # If the tree is visible from at least one edge, increase visible_count.
        if up_visible or down_visible or left_visible or right_visible:
            visible_count += 1

        # Calculate scenic value and determine whether it is the biggest
        scenic_value = up * down * left * right
        if scenic_value > max_scenic:
            max_scenic = scenic_value

print("Part 1:", visible_count)
print("Part 2:", max_scenic)
