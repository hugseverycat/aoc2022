from collections import defaultdict

filename = 'inputs/day9.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip().split(' ') for line in f]

moves = []
head_location = (0, 0)
tail_location = (0, 0)

head_visited = defaultdict(int)
tail_visited = defaultdict(int)
head_visited[head_location] = 1
tail_visited[tail_location] = 1

for this_line in lines:
    moves.append([this_line[0], int(this_line[1])]) # R 17


def move_head(direction, c_pos):
    d_map = {'R': [1, 0],
             'L': [-1, 0],
             'U': [0, -1],
             'D': [0, 1]}
    # Nasty list comprehension:
    #  1. List of all items in d_map[direction] multiplied by distance
    #  2. Zipped with c_pos to allow us to add the lists together item-wise
    #  3. Finally, add current + increase from the zipped list
    #return tuple([current + increase for current, increase in zip(c_pos, [d * distance for d in d_map[direction]])])
    return tuple([position + increase for position, increase in zip(c_pos, d_map[direction])])

def move_tail(t_pos, h_pos):
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


#print(move_head('U', (3, 3)))
#print(move_tail((0,0), (3, 7)))

for this_move in moves:
    move_dir, total_steps = this_move
    #print(f"Starting move: {this_move}. Head: {head_location}; Tail: {tail_location}")
    for i in range(total_steps):
        head_location = move_head(move_dir, head_location)
        #print(f"  Head moved to {head_location}")
        new_tail = move_tail(tail_location, head_location)
        if new_tail != tail_location:
            tail_location = new_tail
            tail_visited[tail_location] += 1
            #print(f"  Tail followed to {tail_location}")
        else:
            #print(f"  Tail at {tail_location} did not move")
            pass
    #print("--------")


"""for i, t in enumerate(tail_visited):
    print(f"{i+1}. {t}: {tail_visited[t]}")"""

print(f"Part 1: {len(tail_visited)}")
