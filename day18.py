from collections import defaultdict

filename = 'inputs/day18.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [l.rstrip() for l in f]

# 2,2,2
lava_cubes = set()
air_cubes = defaultdict(list)


for this_cube in lines:
    coords = tuple([int(n) for n in this_cube.split(',')])
    lava_cubes.add(coords)

surface_area = 0
min_x = min_y = min_z = 20
max_x = max_y = max_z = 0
min_cube = (0, 0, 0)

for this_cube in lava_cubes:
    x, y, z = this_cube
    if x < min_x:
        min_x = x
    if y < min_y:
        min_y = y
    if z < min_z:
        min_z = z
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    if z > max_z:
        max_z = z
    total_neighbors = 0
    if (x+1, y, z) not in lava_cubes:
        air_cubes[(x + 1, y, z)] = []
        total_neighbors += 1
    if (x-1, y, z) not in lava_cubes:
        air_cubes[(x - 1, y, z)] = []
        total_neighbors += 1
    if (x, y+1, z) not in lava_cubes:
        air_cubes[(x, y+1, z)] = []
        total_neighbors += 1
    if (x, y-1, z) not in lava_cubes:
        air_cubes[(x, y-1, z)] = []
        total_neighbors += 1
    if (x, y, z+1) not in lava_cubes:
        air_cubes[(x, y, z+1)] = []
        total_neighbors += 1
    if (x, y, z-1) not in lava_cubes:
        air_cubes[(x, y, z-1)] = []
        total_neighbors += 1

    surface_area += total_neighbors

print(f"x: {min_x}-{max_x}; y: {min_y}-{max_y}; z: {min_z}-{max_z}")
print(f"Part 1: {surface_area}")
