import re

filename = 'inputs/day4.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [list(map(int, re.split('-|,', line.rstrip()))) for line in f]

overlap_count_1 = 0
overlap_count_2 = 0

for this_pair in lines:
    elf_1 = set([n for n in range(this_pair[0], this_pair[1] + 1)])
    elf_2 = set([n for n in range(this_pair[2], this_pair[3] + 1)])

    if elf_1.issubset(elf_2) or elf_2.issubset(elf_1):
        overlap_count_1 += 1

    if not elf_1.isdisjoint(elf_2):
        overlap_count_2 += 1

print("Part 1:", overlap_count_1)
print("Part 2:", overlap_count_2)
