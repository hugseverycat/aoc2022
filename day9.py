filename = 'inputs/day9.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip().split(' ') for line in f]


def move_head(direction, c_pos):
    # Moves the head knot in the indicated direction 1 step
    d_map = {'R': [1, 0],
             'L': [-1, 0],
             'U': [0, -1],
             'D': [0, 1]}
    # Zip allows me to add the 2 arrays together
    # For example if direction is 'L' and c_pos is (3, 3) then the result is (2, 3)
    return tuple([position + increase for position, increase in zip(c_pos, d_map[direction])])


def move_tail(t_pos, h_pos):
    # Determines whether tail (t_pos) is no longer adjacent to head (h_pos)
    # then moves the tail towards the head if necessary

    # y - x for each x and y in t_pos and h_pos
    p_difference = [y - x for x, y in zip(t_pos, h_pos)]
    if max([abs(p) for p in p_difference]) <= 1:
        return t_pos
    move_direction = []
    # tail can only move 1 step so we'll get the direction of the move by
    # dividing the difference by the absolute value of itself.
    for p in p_difference:
        if p == 0:  # can't divide by zero!
            move_direction.append(0)
        else:
            move_direction.append(p//abs(p))
    return tuple([current + increase for current, increase in zip(t_pos, move_direction)])


def solve(num_knots: int):
    moves = []
    knot_list = [(0, 0) for _ in range(num_knots)]
    tail_visited = set()

    for this_line in lines:
        moves.append([this_line[0], int(this_line[1])])  # R 17

    # Approach: Move the head 1 step in given direction, then loop thru each
    # knot in the tail and move them if necessary. Repeat for the total steps.
    # Add the position of the final knot to the tail_visited set.
    for this_move in moves:
        move_dir, total_steps = this_move
        for _ in range(total_steps):
            knot_list[0] = move_head(move_dir, knot_list[0])
            for i in range(1, num_knots):
                # Move each tail relative to the knot ahead of it in the list
                knot_list[i] = move_tail(knot_list[i], knot_list[i-1])
            tail_visited.add(knot_list[-1])  # Set automatically ignores dupes
    return len(tail_visited)


print(f"Part 1: {solve(2)}")
print(f"Part 2: {solve(10)}")
