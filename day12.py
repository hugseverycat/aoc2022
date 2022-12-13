from queue import Queue

filename = 'inputs/day12.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]


class Node:
    def __init__(self, pos, elev):
        self.pos = pos
        self.elev = elev
        self.paths = []

    def add_path(self, new_path):
        if new_path not in self.paths:
            self.paths.append(new_path)

    def generate_paths(self, map_c):
        my_x, my_y = self.pos
        p_paths = [(my_x, my_y + 1), (my_x, my_y - 1), (my_x - 1, my_y), (my_x + 1, my_y)]
        for p in p_paths:
            if p in map_c:
                if map_c[p].elev <= self.elev + 1:
                    self.paths.append(p)

    def print_paths(self):
        print(f"Paths for node {self.pos} at elevation {self.elev}:")
        for p in self.paths:
            print(p)

    def __str__(self):
        return f"Node {self.pos} at elevation {self.elev}"


def get_shortest_path(heightmap, start_position, goal_position):
    # This code copy-pasted then modified from
    # https://www.redblobgames.com/pathfinding/a-star/introduction.html
    # Simple breadth-first search (BFS)

    frontier = Queue()
    frontier.put(start_position)
    came_from = dict()
    came_from[start_position] = None

    while not frontier.empty():
        current_position = frontier.get()

        if current_position == goal_position:
            break

        for next_position in heightmap[current_position].paths:
            if next_position not in came_from:
                frontier.put(next_position)
                came_from[next_position] = current_position

    current_position = goal_position
    path = []
    while current_position != start_position:
        path.append(current_position)
        try:
            # For some reason, this gives KeyError if there's no path from
            # start_position to goal_position
            current_position = came_from[current_position]
        except KeyError:
            # We're returning the came_from dictionary because any nodes we
            # tried to visit will also not have a path to goal_position, so
            # we can avoid checking them in the future
            return False, came_from

    return True, len(path)


h_map = {}

for y, this_row in enumerate(lines):
    for x, this_c in enumerate(this_row):
        if this_c == 'S':
            start_pos = (x, y)
            elevation = 0
        elif this_c == 'E':
            goal_pos = (x, y)
            elevation = 25
        else:
            elevation = ord(this_c) - 97
        h_map[(x, y)] = Node((x, y), elevation)

for h in h_map:
    h_map[h].generate_paths(h_map)

part_2_paths = []
unreachables = set()

for this_coord in h_map:
    if this_coord not in unreachables:
        if h_map[this_coord].elev == 0:
            found, result = get_shortest_path(h_map, this_coord, goal_pos)
            if found:
                part_2_paths.append(result)
            else:
                for c in result:
                    unreachables.add(c)
            if this_coord == start_pos:
                part_1 = result


print(f"Part 1: {part_1}")
print(f"Part 2: {min(part_2_paths)}")
