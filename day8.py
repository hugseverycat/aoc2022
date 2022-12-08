filename = 'inputs/day8.txt'
filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]

tree_map = {}
height = len(lines)
width = len(lines[0])
debug_coord = (0,2)

for y, this_row in enumerate(lines):
    for x, this_col in enumerate(this_row):
        tree_map[(x, y)] = this_col


def is_visible(coord, t_map, h, w):
    cx = coord[0]
    cy = coord[1]

    scenic_score = 1
    visible_dirs = {'top': True,
                    'bottom': True,
                    'left': True,
                    'right': True}
    temp_score = 1
    if coord == debug_coord:
        print("Checking", coord, "to the left:")
    for this_x in range(cx-1, 0, -1):
        if t_map[(this_x, cy)] >= t_map[coord]:
            if coord == debug_coord:
                print("  blocked at", (this_x, cy), "by height", t_map[(this_x, cy)])
            visible_dirs['left'] = False
            break
        if coord == debug_coord:
            print("  sees past", (this_x, cy), "with height", t_map[(this_x, cy)])
        temp_score += 1
        if coord == debug_coord:
            print("  visibility count is now", temp_score)
    if coord == debug_coord:
        print(" ", debug_coord, t_map[debug_coord], "can see", temp_score, "trees to the left")
        print()

    scenic_score *= temp_score

    temp_score = 1
    if coord == debug_coord:
        print("Checking", coord, "to the top:")
    for this_y in range(cy-1, 0, -1):
        if t_map[(cx, this_y)] >= t_map[coord]:
            if coord == debug_coord:
                print("  blocked at", (cx, this_y), "by height", t_map[(cx, this_y)])
                print("  final visibility is", temp_score)
            visible_dirs['top'] = False
            break
        if coord == debug_coord:
            print("  sees past", (cx, this_y), "with height", t_map[(cx, this_y)])
        temp_score += 1
        if coord == debug_coord:
            print("  visibility count is now", temp_score)
    if coord == debug_coord:
        print(" ", debug_coord, t_map[debug_coord], "can see", temp_score, "trees to the top")
        print("---")
    scenic_score *= temp_score

    temp_score = 1
    if coord == debug_coord:
        print("Checking", coord, "to the right:")
    for this_x in range(cx + 1, w-1):
        if t_map[(this_x, cy)] >= t_map[coord]:
            visible_dirs['right'] = False
            if coord == debug_coord:
                print("  blocked at", (this_x, cy), "by height", t_map[(this_x, cy)])
                print("  final visibility is", temp_score)
            break
        temp_score += 1
        if coord == debug_coord:
            print("  sees past", (this_x, cy), "with height", t_map[(this_x, cy)])
            print("  visibility count is now", temp_score)
    if coord == debug_coord:
        print(" ", debug_coord, t_map[debug_coord], "can see", temp_score, "trees to the right")
        print("---")
    scenic_score *= temp_score

    temp_score = 1
    if coord == debug_coord:
        print("Checking", coord, "to the bottom:")
    for this_y in range(cy + 1, h-1):
        if t_map[(cx, this_y)] >= t_map[coord]:
            visible_dirs['bottom'] = False
            if coord == debug_coord:
                print("  blocked at", (cx, this_y), "by height", t_map[(cx, this_y)])
                print("  final visibility is", temp_score)
            break
        temp_score += 1
        if coord == debug_coord:
            print("  sees past", (cx, this_y), "with height", t_map[(cx, this_y)])
            print("  visibility count is now", temp_score)
    if coord == debug_coord:
        print(" ", debug_coord, t_map[debug_coord], "can see", temp_score, "trees to the bottom")
        print("---")
    scenic_score *= temp_score

    return (visible_dirs, scenic_score)


visible_count = 0
max_scenic_score = 0
max_coord = None
for c in tree_map:
    v, s = is_visible(c, tree_map, height, width)
    if s > max_scenic_score:
        max_scenic_score = s
        max_coord = c
    if c == debug_coord:
        print("-----")
        print(c, tree_map[c], "has a scenic score of", s)
    vis_dirs = [d for d in v if v[d] is True]
    if vis_dirs:
        if c == debug_coord:
            print(c, tree_map[c], "is visible from", [d for d in v if v[d] is True])
        visible_count += 1
    else:
        pass
        #print(c, tree_map[c], "is not visible")
    #print("***")

print("Part 1:", visible_count)
print("Part 2:", max_scenic_score)
print(max_coord)



"""for y in range(len(lines)):
    print_line = ''
    for x in range(len(lines[0])):
        print_line += tree_map[(x, y)]
    print(print_line)"""