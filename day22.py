import re

filename = 'inputs/day22.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    input_list = [line.rstrip() for line in f]


directions = input_list[-1]
directions = re.findall("\d+|[LR]", directions)

# Get the map part of the input
board_map = input_list[:-2]

max_y = len(board_map)
max_x = 0
for this_line in board_map:
    if len(this_line) > max_x:
        max_x = len(this_line)

# Fill every horizontal line with whitespace so they are all the same length
# This way we don't have to worry about index errors
for i in range(len(board_map)):
    board_map[i] = board_map[i].ljust(max_x, ' ')

current_position = (board_map[0].find('.'), 0)
current_direction = (1, 0)


def print_board(board: list, c_pos=None):
    if c_pos is not None:
        cx, cy = c_pos
    for y in range(len(board)):
        line = ''
        for x in range(len(board[0])):
            if c_pos is not None:
                if (x, y) == (cx, cy):
                    line += '@'
            else:
                line += board[y][x]
        print(line)

    print()


def do_move(c_pos: tuple, c_dir: tuple, move: str, board: list):
    if move == 'L':
        if c_dir == (1, 0):
            c_dir = (0, -1)
        elif c_dir == (0, -1):
            c_dir = (-1, 0)
        elif c_dir == (-1, 0):
            c_dir = (0, 1)
        elif c_dir == (0, 1):
            c_dir = (1, 0)
        return c_pos, c_dir
    elif move == 'R':
        if c_dir == (1, 0):
            c_dir = (0, 1)
        elif c_dir == (0, 1):
            c_dir = (-1, 0)
        elif c_dir == (-1, 0):
            c_dir = (0, -1)
        elif c_dir == (0, -1):
            c_dir = (1, 0)
        return c_pos, c_dir
    else:
        move = int(move)
        cx, cy = c_pos
        mx, my = c_dir
        #print(f"{c_pos} Moving {move} in this direction: {c_dir}:")
        for _ in range(move):
            nx = (cx + mx) % max_x
            ny = (cy + my) % max_y
            while board[ny][nx] == ' ':
                nx = (nx + mx) % max_x
                ny = (ny + my) % max_y
            if board[ny][nx] == '#':
                c_pos = (cx, cy)
                return c_pos, c_dir
            elif board[ny][nx] == '.':
                cx, cy = (nx, ny)

        c_pos = cx, cy
        return c_pos, c_dir

#print_board(board_map, current_position)
#print(f"Start position: {current_position}")
for this_move in directions:
    current_position, current_direction = do_move(current_position, current_direction, this_move, board_map)


#print_board(board_map, current_position)
#print(f"End position: {current_position}")

password = (current_position[1] + 1) * 1000 + (current_position[0] + 1) * 4
if current_direction == (1, 0):
    password += 0
elif current_position == (0, 1):
    password += 1
elif current_position == (-1, 0):
    password += 2
elif current_position == (0, -1):
    password += 3

print(password)
print(f"Correct test answer: 6032")
print(f"Correct part 1 answer: 1484")