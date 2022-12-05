from collections import deque
import re

filename = 'inputs/day5.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]

part = 2
instructions = []
stacks = [deque() for i in range(9)]
temp_stacks = []
input_instructions = False

# Parse input
for this_line in lines:
    if this_line == '':
        input_instructions = True
    elif input_instructions:
        instructions.append([int(a) for a in re.findall('\d+', this_line)])
    else:
        temp_stacks.append(this_line)

for t in temp_stacks:
    # The letters are at specific locations in the string so we're just grabbing
    # them by their known locations (n)
    for i in range(9):
        n = i * 4 + 1
        # try-except to skip when a particular string doesn't have anything in the higher
        # numbered stacks and thus is shorter in length. also test input.
        try:
            if t[n] == '1':
                # Don't handle the line that numbers the stacks
                break
            if t[n] != ' ':
                stacks[i].appendleft(t[n])
        except IndexError:
            break

# Do stuff
for this_inst in instructions:
    # move X from Y to Z
    temp = deque()
    for i in range(this_inst[0]):
        if part == 1:
            stacks[this_inst[2] - 1].append(stacks[this_inst[1] - 1].pop())
        else:
            temp.appendleft(stacks[this_inst[1] - 1].pop())
    if part == 2:
        stacks[this_inst[2] - 1].extend(temp)

solution = ''
for s in stacks:
    # try-except here to handle test input that doesn't have 9 stacks
    try:
        solution += s.pop()
    except IndexError:
        pass

print(f"Part {part}:", solution)
