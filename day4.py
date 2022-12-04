import re

filename = 'inputs/day4.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]

overlap_count_1 = 0
overlap_count_2 = 0

for this_pair in lines:
    pairs = [int(f) for f in re.split('-|,', this_pair)]
    elf_1 = [pairs[0], pairs[1]]
    elf_2 = [pairs[2], pairs[3]]

    if elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]:
        overlap_count_1 += 1
        overlap_count_2 += 1
    elif elf_2[0] >= elf_1[0] and elf_2[1] <= elf_1[1]:
        overlap_count_1 += 1
        overlap_count_2 += 1
    elif elf_1[0] <= elf_2[0] <= elf_1[1]:
        overlap_count_2 += 1
    elif elf_1[0] <= elf_2[1] <= elf_1[1]:
        overlap_count_2 += 1
    elif elf_2[0] <= elf_1[0] <= elf_2[1]:
        overlap_count_2 += 1
    elif elf_2[0] <= elf_1[1] <= elf_2[1]:
        overlap_count_2 += 1

print("Part 1:", overlap_count_1)
print("Part 2:", overlap_count_2)
