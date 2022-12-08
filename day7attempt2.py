filename = 'inputs/day7.txt'
#filename = 'inputs/test.txt'


class Node:
    def __init__(self, name: str, parent, size: int):
        self.name = name
        self.size = size
        self.children = []
        self.parent = parent
        self.update_parent(parent)

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_child_by_name(self, child_name):
        for c in self.children:
            if c.name == child_name:
                return c
        return None

    def update_parent(self, p):
        if p is not None:
            p.add_child(self)

    def __str__(self):
        return "Node: " + self.name


with open(filename) as f:
    lines = [line.rstrip() for line in f]

nodes = {'dir_list': [], 'file_list': [], 'root': Node('root', None, None)}
current_dir = nodes['root']

for this_line in lines:
    if this_line[:4] == '$ cd':
        change_to = this_line[5:]
        if change_to == '/':
            current_dir = nodes['root']
        elif change_to == '..':
            current_dir = current_dir.parent
        else:   # $ cd a
            current_dir = current_dir.get_child_by_name(change_to)
    elif this_line[:4] == '$ ls':
        # don't do anything
        continue
    else:
        if this_line[0:3] == 'dir':  # dir a
            dir_name = this_line[4:]
            nodes['dir_list'].append(Node(dir_name, current_dir, None))  # All directories start with size None
        else:  # 14848514 b.txt
            file_size, file_name = this_line.split(' ')
            nodes['file_list'].append(Node(file_name, current_dir, int(file_size)))


def calculate_size(n_list, this_d):
    # A recursive function that finds directories with no size, then looks through its children
    # and calculates its total size.
    dir_size = 0
    for this_c in this_d.children:
        if this_c.size is None:  # This means this is a directory we haven't sized yet
            this_c.size = calculate_size(n_list, this_c)  # Recursively calculate size of child directory
        dir_size += this_c.size  # Add the size of this child directory or file to the total
    return dir_size


# Not only calculates the size of the root directory but the recursive function
# will also populate the size of all subdirectories
nodes['root'].size = calculate_size(nodes, nodes['root'])

# OK the hard work is done, let's find the directories that match our criteria!
part_1 = 0
space_needed = 30000000 - (70000000 - nodes['root'].size)
smallest_dir_size = nodes['root'].size

for this_dir in nodes['dir_list']:
    if this_dir.size <= 100000:
        part_1 += this_dir.size
    if space_needed <= this_dir.size < smallest_dir_size:
        smallest_dir_size = this_dir.size

print("Part 1:", part_1)
print("Part 2:", smallest_dir_size)
