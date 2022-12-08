filename = 'inputs/day8.txt'
filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]

tree_map = {}
height = len(lines)
width = len(lines[0])
debug_coord = (-1,1)

for y, this_row in enumerate(lines):
    for x, this_col in enumerate(this_row):
        tree_map[(x, y)] = this_col


def is_visible(coord, t_map, h, w):
    cx = coord[0]
    cy = coord[1]
    visible = 4
    scenic_score = 1

    if cx in (0, w-1) or cy in (0, h-1):
        #print(coord, "is on the edge")
        scenic_score = 0
    else:
        print(coord, "is in the interior")
        temp_score = 1
        for x in range(cx+1, w-1):
            if t_map[(x, cy)] >= t_map[coord]:
                visible -= 1
                break
            temp_score += 1
        scenic_score *= temp_score
        if coord == debug_coord:
            print(coord, "sees", temp_score, "to the right")
            print("---")

        temp_score = 1
        for y in range(cy+1, h-1):
            if t_map[(cx, y)] >= t_map[coord]:
                visible -= 1
                break
            temp_score += 1
        scenic_score *= temp_score
        if coord == debug_coord:
            print(coord, "sees", temp_score, "to the bottom")
            print("---")

        temp_score = 1
        for x in range(cx-1, 0, -1):
            if t_map[(x, cy)] >= t_map[coord]:
                visible -= 1
                break
            temp_score += 1
        scenic_score *= temp_score
        if coord == debug_coord:
            print(coord, "sees", temp_score, "to the left")
            print("---")

        temp_score = 1
        for y in range(cy-1, 0, -1):
            if t_map[(cx, y)] >= t_map[coord]:
                visible -= 1
                break
            temp_score += 1
        scenic_score *= temp_score
        if coord == debug_coord:
            print(coord, "sees", temp_score, "to the top")
            print("---")

        if visible:
            print(visible)
            print(coord, "is visible")
            print("---")
        else:
            print(visible)
            print(coord, "is not visible")
            print("---")

    return (visible, scenic_score)


visible_count = 0
max_scenic_score = 0
max_coord = None
for c in tree_map:
    v, s = is_visible(c, tree_map, height, width)
    if v:
        visible_count += 1
    if s > max_scenic_score:
        max_scenic_score = s

print("Part 1:", visible_count)
print("Part 2:", max_scenic_score)
print(max_coord)



"""for y in range(len(lines)):
    print_line = ''
    for x in range(len(lines[0])):
        print_line += tree_map[(x, y)]
    print(print_line)"""