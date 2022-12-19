from collections import deque

filename = 'inputs/day18.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [l.rstrip() for l in f]

# Fill the lava cubes set with coordinates from the input
lava_cubes = set()
for this_cube in lines:
    coords = tuple([int(n) for n in this_cube.split(',')])
    lava_cubes.add(coords)

# Create a larger cube of "air cubes" which is every cube from
# -1 to 21 in the x, y, and z direction that isn't a lava cube
air_cubes = {}
min_c = -1
max_c = 21

for x in range(min_c, max_c):
    for y in range(min_c, max_c):
        for z in range(min_c, max_c):
            if (x, y, z) not in lava_cubes:
                air_cubes[(x, y, z)] = False


def get_surface_area(cubes):
    # Takes an iterable of cubes and calculates its surface area
    s_area = 0
    for this_cube in cubes:
        x, y, z = this_cube

        total_neighbors = 0
        possible_neighbors = [(x+1, y, z), (x-1, y, z), (x, y+1, z),
                              (x, y-1, z), (x, y, z+1), (x, y, z-1)]

        # For each possible neighboring coord, if it doesn't have a neighbor
        # in the cubes iterable, then increase the surface area by 1
        for p in possible_neighbors:
            if p not in cubes:
                total_neighbors += 1

        s_area += total_neighbors
    return s_area


def flood_fill(start_c: tuple, air_c: dict):
    # Goes thru all cubes in air_c connected to start_c and "fills" them
    # Unfilled cubes are False, filled cubes are True

    queue = deque()
    # initialize queue with start coordinate
    queue.append(start_c)

    while queue:
        # Pull from the front of the queue
        coord = queue.popleft()
        # Set it to filled
        air_c[coord] = True
        # Find all its unfilled, non-lava neighbors and add to queue
        cx, cy, cz = coord
        directions = [(cx - 1, cy, cz), (cx + 1, cy, cz), (cx, cy + 1, cz),
                      (cx, cy - 1, cz), (cx, cy, cz + 1), (cx, cy, cz - 1)]

        for d in directions:
            if d in air_c and not air_c[d] and d not in queue:
                queue.append(d)


# This stuff is for part 2, where we flood fill starting with a far corner
start_coord = (-1, -1, -1)
flood_fill(start_coord, air_cubes)
inner_cubes = [c for c in air_cubes if air_cubes[c] is False]
inner_cubes_sa = get_surface_area(inner_cubes)

part_1_surface_area = get_surface_area(lava_cubes)
part_2_surface_area = part_1_surface_area - inner_cubes_sa

print(f"Part 1: {part_1_surface_area}")
print(f"Part 2: {part_2_surface_area}")
