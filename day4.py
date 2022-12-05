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

assignments = []
with open('inputs/day4.txt', 'r') as input:
    for line in input:
        line = line.strip()
        assignments.append(line.split(','))

contains = 0
for pair in assignments:
    #print(pair)
    elf1, elf2 = pair[0], pair[-1]
    #print(elf1, elf2)

    start1, end1 = elf1.split('-')
    #print(start1,end1)

    start2, end2 = elf2.split('-')
    print(type(start2), end2)
    #break
    # check if elf 1's range contains elf 2's range
    if start1 <= start2 and end1 >= end2:
        contains = contains + 1
        #print(pair)
    # check if elf 2's range contains elf 1's range
    elif start2 <= start1 and end2 >= end1:
        contains = contains + 1
        #print(pair)

print(contains)
