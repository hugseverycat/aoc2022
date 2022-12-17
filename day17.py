from tqdm import tqdm

filename = 'inputs/day17.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    jet_pattern = f.readline()


def new_rock(h: int, n: int) -> list:
    if n == 0:      # -
        return [(2, h+3), (3, h+3), (4, h+3), (5, h+3)]
    elif n == 1:    # +
        return [(2, h+4), (3, h+4), (4, h+4), (3, h+5), (3, h+3)]
    elif n == 2:    # J
        return [(2, h+3), (3, h+3), (4, h+3), (4, h+4), (4, h+5)]
    elif n == 3:    # I
        return [(2, h+3), (2, h+4), (2, h+5), (2, h+6)]
    elif n == 4:    # o
        return [(2, h+3), (3, h+3), (2, h+4), (3, h+4)]


def print_tetris(c: dict, h:int):
    for y in range(h+3, -1, -1):
        print_line = '|'
        for x in range(7):
            if y in c[x]:
                print_line += '@'
            else:
                print_line += '.'
        print_line += '|'
        print(print_line)
    print("+-------+")


def update_pos(c: dict[set], r:list) -> dict:
    for this_coord in r:
        rx, ry = this_coord
        c[rx].add(ry)
    return c


def get_height(c:dict) -> int:
    h = 0
    for this_column in c:
        if len(c[this_column]):
            m = max(c[this_column])
            if m > h:
                h = m
    return h + 1


columns = {
    0: set(),
    1: set(),
    2: set(),
    3: set(),
    4: set(),
    5: set(),
    6: set()
}



"""
my_rock = new_rock(0, 4)
for this_coord in my_rock:
    rx, ry = this_coord
    columns[rx].add(ry)

print_tetris(columns, 8)
"""


height = 0
jet = 0

for rock_count in tqdm(range(2022)):
    #print(f"Rock {rock_count}:")
    rock_order = rock_count % 5
    rock = new_rock(height, rock_order)
    at_rest = False
    while not at_rest:
        # check if rock is moved by jet
        try:
            jp = jet_pattern[jet]
        except IndexError:
            jet = 0
            jp = jet_pattern[jet]
        horiz = True
            # update temp rock position
        if jp == '<':
            temp_rock = [(tx - 1, ty) for (tx, ty) in rock]
        elif jp == '>':
            temp_rock = [(tx + 1, ty) for (tx, ty) in rock]
            # check whether temp rock position collides with wall or another rock
        for this_coord in temp_rock:
            tx, ty = this_coord
            if tx < 0 or tx >= 7 or ty in columns[tx]:
                horiz = False
                #print(f"Rock {rock_count} does not move {jet_pattern[jet]}")
        if horiz:
            rock = temp_rock
            #print(f"Rock {rock_count} moves {jet_pattern[jet]}")
        else:
            horiz = True
        jet += 1

            # move down and check if rock comes to rest
        temp_rock = [(tx, ty - 1) for (tx, ty) in rock]
        for this_coord in temp_rock:
            tx, ty = this_coord
            if ty < 0 or ty in columns[tx]:
                #print(f"Rock {rock_count} comes to rest")
                at_rest = True
                break
        if not at_rest:
            #print(f"Rock {rock_count} falls 1 unit")
            rock = temp_rock

    # update columns with rock's final position
    columns = update_pos(columns, rock)
    height = get_height(columns)
    #print(f"new height: {height}")
    #print(f"Rock {rock_count} final position:")
    #print_tetris(columns, height)
    #print()
print(height)