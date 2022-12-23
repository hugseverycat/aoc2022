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

# Pad every horizontal line with whitespace so that they are all the same length
# This way we don't have to worry about index errors
# (For part 2 we should never visit these spots)
for i in range(len(board_map)):
    board_map[i] = board_map[i].ljust(max_x, ' ')

# Find the first valid position from left in the top row
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


def corner_turn(n_pos: tuple, c_dir: tuple):
    #  21
    #  3
    # 54
    # 6
    nx, ny = n_pos

    if c_dir == (1, 0):  # Moving rightward
        if 0 <= ny < 50 and nx == 100:  # Moving from 2 to 1
            # no changes
            pass

        elif 0 <= ny < 50 and nx == 150:  # Moving from 1 to 4
            # Direction changes from R to L
            c_dir = (-1, 0)
            n_pos = (99, 149 - ny)
        elif 50 <= ny < 100 and nx == 100:  # moving from 3 to 1
            # Direction changes from R to U
            c_dir = (0, -1)
            n_pos = (ny + 50, 49)

        elif 100 <= ny < 150 and nx == 100:  # moving from 4 to 1
            # Direction changes from R to L
            c_dir = (-1, 0)
            n_pos = (149, 149 - ny)

        elif 100 <= ny < 150 and nx == 50:  # moving from 5 to 4
            # no change
            pass

        elif 150 <= ny < 200 and nx == 50:  # moving from 6 to 4
            # Direction changes from R to U
            c_dir = (0, -1)
            n_pos = (ny - 100, 149)

    elif c_dir == (-1, 0):  # Moving leftward
        if 0 <= ny < 50 and nx == 99:  # Moving from 1 to 2
            # no changes
            pass

        elif 0 <= ny < 50 and nx == 49:  # Moving from 2 to 5
            # Direction changes from L to R
            c_dir = (1, 0)
            n_pos = (0, 149 - ny)

        elif 50 <= ny < 100 and nx == 49:  # moving from 3 to 5
            # Direction changes from L to D
            c_dir = (0, 1)
            n_pos = (ny - 50, 100)

        elif 100 <= ny < 150 and nx == -1:  # moving from 5 to 2
            # Direction changes from L to R
            c_dir = (1, 0)
            n_pos = (50, 149 - ny)

        elif 100 <= ny < 150 and nx == 49:  # moving from 4 to 5
            # no change
            pass

        elif 150 <= ny < 200 and nx == -1:  # moving from 6 to 2
            # Direction changes from L to D
            c_dir = (0, 1)
            n_pos = (ny - 100, 0)

    elif c_dir == (0, 1):  # Moving downward
        if 100 <= nx < 150 and ny == 50:  # Moving from 1 to 3
            # Direction changes from D to L
            c_dir = (-1, 0)
            n_pos = (99, nx - 50)

        elif 50 <= nx < 100 and ny == 50:  # Moving from 2 to 3
            # No changes
            pass

        elif 50 <= nx < 100 and ny == 100:  # Moving from 3 to 4
            # No changes
            pass

        elif 50 <= nx < 100 and ny == 150:  # Moving from 4 to 6
            # Direction changes from D to L
            c_dir = (-1, 0)
            n_pos = (49, nx + 100)

        elif 0 <= nx < 50 and ny == 150:  # Moving from 5 to 6
            # No changes
            pass

        elif 0 <= nx < 50 and ny == 200:  # Moving from 6 to 1
            # Direction remains the same
            n_pos = (nx + 100, 0)

    elif c_dir == (0, -1):  # Moving upward
        if 100 <= nx < 150 and ny == -1:  # moving from 1 to 6
            # Direction unchanged
            n_pos = (nx - 100, 199)

        elif 50 <= nx < 100 and ny == -1:  # Moving from 2 to 6
            # Direction changes from U to R
            c_dir = (1, 0)
            n_pos = (0, nx + 100)

        elif 50 <= nx < 100 and ny == 49:  # moving from 3 to 2
            # No changes
            pass

        elif 50 <= nx < 100 and ny == 99:  # moving from 4 to 3
            # No changes
            pass

        elif 0 <= nx < 50 and ny == 99:  # moving from 5 to 3
            # Direction changes from U to R
            c_dir = (1, 0)
            n_pos = (50, nx + 50)

        elif 0 <= nx < 50 and ny == 149:  # moving from 6 to 5
            # No changes
            pass

    return n_pos, c_dir


def do_move(c_pos: tuple, c_dir: tuple, move: str, board: list):
    if move == 'L':
        if c_dir == (1, 0):
            n_dir = (0, -1)
        elif c_dir == (0, -1):
            n_dir = (-1, 0)
        elif c_dir == (-1, 0):
            n_dir = (0, 1)
        elif c_dir == (0, 1):
            n_dir = (1, 0)
        return c_pos, n_dir
    elif move == 'R':
        if c_dir == (1, 0):
            n_dir = (0, 1)
        elif c_dir == (0, 1):
            n_dir = (-1, 0)
        elif c_dir == (-1, 0):
            n_dir = (0, -1)
        elif c_dir == (0, -1):
            n_dir = (1, 0)
        return c_pos, n_dir
    else:
        move = int(move)
        cx, cy = c_pos  # cx, cy, c_pos are only for confirmed moves
        cdx, cdy = c_dir  # confirmed direction of travel
        ndx, ndy = c_dir  # ndx, ndy will hold any unconfirmed changes of direction
                          # for reasons, it starts out as equal to cdx, cdy

        for _ in range(move):
            # Get proposed new position (nx, ny)
            nx = cx + cdx
            ny = cy + cdy

            # Detect if we've turned a corner
            # If so, update the proposed direction and new position
            if (ndx == 1 and nx in (50, 100, 150)) or \
                    (ndy == 1 and ny in (50, 100, 150, 200)):
                (nx, ny), (ndx, ndy) = corner_turn((nx, ny), (ndx, ndy))

            elif (ndx == -1 and nx in (-1, 49, 99)) or \
                    (ndy == -1 and ny in (-1, 49, 99, 149)):
                (nx, ny), (ndx, ndy) = corner_turn((nx, ny), (ndx, ndy))

            # If there's a blockage, stop moving and return the "current" position
            if board[ny][nx] == '#':
                c_pos = (cx, cy)
                c_dir = (cdx, cdy)
                return c_pos, c_dir

            # If this is open board, the new position & direction becomes current.
            elif board[ny][nx] == '.':
                cx, cy = (nx, ny)
                cdx, cdy = (ndx, ndy)

            elif board[ny][nx] == ' ':
                print("We've left the cube somehow")
                print(f"Position: ({nx}, {ny})")
                print(f"previous direction: ({cdx}, {cdy})")
                print(f"new direction: ({ndx}, {ndy})")
                print(f"coming from: ({cx}, {cy})")
                raise IndexError

        # If we reach this code, we've finished moving with no obstacles
        c_pos = cx, cy
        c_dir = cdx, cdy
        return c_pos, c_dir


for this_move in directions:
    current_position, current_direction = \
        do_move(current_position, current_direction, this_move, board_map)

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
