filename = 'inputs/day3.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]


def get_priority(c):
    # A function to convert single characters into priorities
    # ord(c) turns c into its ascii value, which needs to be adjusted to match
    # priorities in the problem stated
    if c.isupper():
        return ord(c) - 38
    return ord(c) - 96


elf_counter = 0
elf_group = []
priority_p1 = 0
priority_p2 = 0

for this_line in lines:
    # Part 1

    # Turning things into sets removes all duplicates
    c_1 = set(this_line[:len(this_line)//2])    # // operator divides and returns an integer
    c_2 = set(this_line[len(this_line)//2:])

    # Find intersection of the sets to get the repeated item
    # next(iter(set_name)) returns the first (only) item in the set
    dup_p1 = next(iter(c_1.intersection(c_2)))
    priority_p1 += get_priority(dup_p1)

    # Part 2
    elf_group.append(this_line)
    if elf_counter == 2:
        # Once we have a set of 3 elves, convert list items to sets and find the intersection
        dup_p2 = next(iter(set(elf_group[0]).intersection(set(elf_group[1]), set(elf_group[2]))))
        priority_p2 += get_priority(dup_p2)
        elf_counter = 0
        elf_group = []
    else:
        elf_counter += 1

print("Part 1:", priority_p1)
print("Part 2:", priority_p2)
