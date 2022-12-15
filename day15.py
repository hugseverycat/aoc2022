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
# Sensor at x=3163363, y=3448163: closest beacon is at x=3102959, y=3443573
min_x = min_y = None
max_x = max_y = 0
sensor_in_range = set()

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


print(min_x, max_x, min_y, max_y)
beacons_and_sensors = beacon_positions.union(set([s for s in sensor_ranges]))
print(len(sensor_in_range))

# Part 1
check_line = 2000000
counter = 0
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

print(counter)


# wrong answers
# 4984495 (too high)
