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
        if print_line == '|@@@@@@@|':
            print_line += f"*********************************{y}"
        print(print_line)
    print("+-------+")


def update_pos(c: dict[set], r: list) -> dict:
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
    # key (0-7) is the column index. value is a set of occupied y coordinates
    0: set(),
    1: set(),
    2: set(),
    3: set(),
    4: set(),
    5: set(),
    6: set()
}

height = 0
jet = 0
states = {}
cycle_state = None
total_rocks = 2022
total_rocks = 1000000000000  # Change this based on part 1 or 2
rock_count = 0
cycle_found = False

while rock_count < total_rocks:
    rock_order = rock_count % 5  # rock_order determines what the rock shape is
    rock = new_rock(height, rock_order)
    at_rest = False
    while not at_rest:
        # get the next jet pattern
        try:
            jp = jet_pattern[jet]
        except IndexError:  # restart jet pattern if we've reached the end
            jet = 0
            jp = jet_pattern[jet]

        # assuming horizontal movement is possible, get its new position
        horiz = True
        if jp == '<':
            temp_rock = [(tx - 1, ty) for (tx, ty) in rock]
        elif jp == '>':
            temp_rock = [(tx + 1, ty) for (tx, ty) in rock]

        # check whether new position collides with wall or another rock
        for this_coord in temp_rock:
            tx, ty = this_coord
            if tx < 0 or tx >= 7 or ty in columns[tx]:
                horiz = False
        # if we can move horizontally, do so
        if horiz:
            rock = temp_rock
        jet += 1

        # try to move down and check if rock comes to rest
        temp_rock = [(tx, ty - 1) for (tx, ty) in rock]
        for this_coord in temp_rock:
            tx, ty = this_coord
            if ty < 0 or ty in columns[tx]:
                at_rest = True
                break
        if not at_rest:
            rock = temp_rock

    # update columns with rock's final position
    columns = update_pos(columns, rock)
    height = get_height(columns)

    # now here begins all the part 2 stuff to check for states!
    # will not interfere with part 1

    if not cycle_found:
        # get the maximum height of each column
        max_cols = []
        for c in columns:
            if columns[c]:
                max_cols.append(max(columns[c]))
            else:
                max_cols.append(-1)

        # adjust the maximum heights so that they are relative to each other
        # so the lowest one will be zero (or -1 for the floor) and the others will
        # be the difference between their height and the lowest.
        min_col = min(max_cols)
        relative_cols = [mc - min_col for mc in max_cols]

        # add the rock order (so what tetris shape this is) and the jet index to the state
        this_state = relative_cols.extend([rock_order, jet])
        this_state = tuple(relative_cols)

        if this_state in states:
            # Cycle found! Now we find the various attributes of the cycle
            cycle_found = True

            # See the 'else' block for definitions of states[this_state]
            rocks_per_cycle = rock_count - states[this_state]['rock']
            height_per_cycle = height - states[this_state]['height']
            remaining_rocks = total_rocks - rock_count
            cycles_remaining = remaining_rocks//rocks_per_cycle
            rock_remainder = remaining_rocks % rocks_per_cycle

            # We have some rocks left to simulate (the remainder) so we calculate the height
            # increase after all the cycles are done, and set the rock_count so that
            # we only have the rock_remainder left to simulate
            height_increase = height_per_cycle * cycles_remaining
            rock_count = total_rocks - rock_remainder

        else:
            states[this_state] = {'rock': rock_count,
                                  'height': height}

    rock_count += 1

print(height + height_increase)
