import re

filename = 'inputs/day15.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    input_lines = [line.rstrip() for line in f]

def manhattan_distance(start_coord: tuple, end_coord: tuple):
    sx, sy = start_coord
    ex, ey = end_coord
    return abs(sy - ey) + abs(sx - ex)

sensor_ranges = {}
beacon_positions = set()

min_x = min_y = None
max_x = max_y = 0

for this_line in input_lines:
    sx, sy, bx, by = [int(n) for n in re.findall("=(-?\d+)", this_line)]
    this_range = manhattan_distance((sx, sy), (bx, by))
    sensor_ranges[(sx, sy)] = this_range
    beacon_positions.add((bx, by))
    if min_y is None or sy < min_y:
        min_y = sy - sensor_ranges[(sx, sy)]
    elif min_x is None or sx < min_x:
        min_x = sx - sensor_ranges[(sx, sy)]
    elif sy > max_y:
        max_y = sy + sensor_ranges[(sx, sy)]
    elif sx > max_x:
        max_x = sx + sensor_ranges[(sx, sy)]


# set of coords that are "occupied"
beacons_and_sensors = beacon_positions.union(set([s for s in sensor_ranges]))

# Part 1
check_line = 2000000
counter = 0

# naive approach: for all the x's in y = checkline, check if its within the range
# of each sensor 1 by 1
for x in range(min_x, max_x + 1):
    in_range = False
    for this_sensor in sensor_ranges:
        this_coord = (x, check_line)
        if this_coord not in beacons_and_sensors and \
                manhattan_distance(this_coord, this_sensor) <= sensor_ranges[this_sensor]:
            in_range = True
            break
    if in_range:
        counter += 1
print(f"Part 1: {counter}")


def walk_perimeter(this_sensor: tuple, s_positions:dict):
    # For part 2 we get which points are just outside each sensor's range
    # The beacon must be on one of these perimeter points
    sx, sy = this_sensor
    s_range = s_positions[this_sensor]
    perimeter_coords = set()
    cx = sx - s_range - 1
    cy = sy
    while cx < sx:
        perimeter_coords.add((cx, cy))
        cx += 1
        cy += 1
    while cy > sy:
        perimeter_coords.add((cx, cy))
        cx += 1
        cy -= 1
    while cx > sx:
        perimeter_coords.add((cx,cy))
        cx -= 1
        cy += 1
    while cy > sy:
        perimeter_coords.add((cx, cy))
        cx -= 1
        cy -= 1

    return perimeter_coords


for s in sensor_ranges:
    perimeter = walk_perimeter(s, sensor_ranges)
    hidden = False

    # For each point on the perimeter, check if its in the target zone
    # then check it against the manhattan distance of each sensor
    # if its not within any sensor's range, hooray, we're done!!
    for p in perimeter:
        x, y = p
        if 0 <= x <= 4000000 and 0 <= y <= 4000000:
            hidden = True
            for this_sensor in sensor_ranges:
                if manhattan_distance(p, this_sensor) <= sensor_ranges[this_sensor]:
                    hidden = False
                    break
            if hidden:
                distress_beacon = p
                break
    if hidden:
        break

print(f"Part 2: {4000000 * distress_beacon[0] + distress_beacon[1]}")
