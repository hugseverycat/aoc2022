from tqdm import tqdm
from collections import deque

filename = 'inputs/day17.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    jet_pattern = deque(f.readline())


def new_rock(h: int, n: int) -> list:
    if n == 0:  # -
        return [(2, h + 3), (3, h + 3), (4, h + 3), (5, h + 3)]
    elif n == 1:  # +
        return [(2, h + 4), (3, h + 4), (4, h + 4), (3, h + 5), (3, h + 3)]
    elif n == 2:  # J
        return [(2, h + 3), (3, h + 3), (4, h + 3), (4, h + 4), (4, h + 5)]
    elif n == 3:  # I
        return [(2, h + 3), (2, h + 4), (2, h + 5), (2, h + 6)]
    elif n == 4:  # o
        return [(2, h + 3), (3, h + 3), (2, h + 4), (3, h + 4)]


def print_tetris(t_map):
    for this_row in reversed(t_map):
        if ''.join(this_row) == '@@@@@@@':
            print(''.join(this_row) + '****************')
        else:
            print(''.join(this_row))
    print("-------")



def update_tetris(t_map: list, rck: list):
    max_y = max([r[1] for r in rck])
    if max_y >= len(t_map) - 10:
        t_map.extend([['.' for _ in range(7)] for _ in range(10)])
        #print_tetris(t_map)
        #raise IndexError
    for c in rck:
        cx, cy = c
        t_map[cy][cx] = '@'
    return t_map

#update_tetris([], [(1, 2), (3, 4), (5, 6)])


goal_rocks = 2022
total_height = 0
grid_height = 10
working_height = total_height
tetris = [['.' for _ in range(7)] for _ in range(grid_height)]
height_list = ''
height_buffer = ''

for rock_count in tqdm(range(goal_rocks)):
    #break
    #   Create a new rock
    rock = new_rock(working_height, rock_count % 5)
    #print(f"Rock #{rock_count} created")
    at_rest = False
    while not at_rest:
        # While rock is not at rest:

        #   Get proposed position after jet blowing and rotate jet pattern
        j = jet_pattern[0]
        if j == '<':
            temp_rock = [(tx - 1, ty) for (tx, ty) in rock]
        else:  # j == '>'
            temp_rock = [(tx + 1, ty) for (tx, ty) in rock]
        jet_pattern.rotate(-1)

        #   Check if there's a collision
        move_horiz = True
        for coord in temp_rock:
            tx, ty = coord
            try:
                if tx < 0 or tx >= 7 or tetris[ty][tx] == '@':
                    #print(f"Rock does not move {j}")
                    move_horiz = False
                    break
            except:
                print_tetris(tetris)
                #print(temp_rock)
                #print(f"{tx}, {ty}, {len(tetris)}")
                raise

        #   Update rock position if necessary
        if move_horiz:
            #print(f"Rock moves {j}")
            rock = temp_rock

        #   Get proposed position after falling
        temp_rock = [(tx, ty - 1) for (tx, ty) in rock]

        #   Check if there's a collision
        for coord in temp_rock:
            tx, ty = coord
            if ty < 0 or tetris[ty][tx] == '@':
                #print(f"Rock comes to rest")
                at_rest = True
                break

        #   Update rock position if no collision
        if not at_rest:
            rock = temp_rock
            #print(f"Rock falls 1 position")
    # Update the map
    tetris = update_tetris(tetris, rock)


    # Get new height from maximum y in the rock
    height_increase = max([c[1] for c in rock]) - working_height
    if height_increase >= 0:
        height_increase += 1
        working_height += height_increase
        total_height += height_increase
    else:
        height_increase = 0
    height_list += str(height_increase)
    height_buffer += str(height_increase)
    if len(height_buffer) > 30:
        height_buffer = height_buffer[1:]
        if height_buffer in height_list[:30]:
            print(f"repetition found at {rock_count}")
    #print(f"Rock {rock_count}: {working_height} (+{height_increase})")



    # Check for filled lines

        # Lop off lower lines

    # Adjust working height

#print_tetris(tetris)
#print(working_height)
print(height_list)
