with open('day1.txt') as f:
    lines = [line.rstrip() for line in f]

elf_sums = []
this_elf = 0

for line in lines:
    if line == '':
        elf_sums.append(this_elf)
        this_elf = 0
    else:
        this_elf += int(line)

elf_sums.sort(reverse=True)
print(f"Part 1: {elf_sums[0]}")
print(f"Part 2: {sum(elf_sums[0:3])}")
