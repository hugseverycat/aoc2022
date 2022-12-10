filename = 'inputs/day10.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]

inst_list = []
for this_line in lines:
    if "noop" in this_line:
        inst_list.append(None)
    else:
        this_inst = this_line.split(' ')
        inst_list.append(int(this_inst[1]))  # Just get the number part

x_register = 1
cycle = 1
ci = 0  # To track which instruction we are on (index of inst_list)
total_inst = len(inst_list)
addx_active = False
signal_strength = 0
screen = ''

while ci < total_inst:
    # We draw before doing anything else
    if (cycle - 1) % 40 in range(x_register - 1, x_register + 2):
        screen += '⬜'
    else:
        screen += '⬛'

    # Now process the commands
    if addx_active:  # Finish the addx command
        x_register += inst_list[ci]
        addx_active = False
        ci += 1
    elif inst_list[ci] is None:  # Do nothing and move to next inst
        ci += 1
    else:  # We are beginning a new addx
        addx_active = True

    cycle += 1

    if (cycle - 20) % 40 == 0:  # Do part 1 calculations
        signal_strength += cycle * x_register

print(f"Part 1: {signal_strength}")

for screen_line in [screen[y:y+40] for y in [x * 40 for x in range(0, 6)]]:
    print(screen_line)
