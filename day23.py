from collections import defaultdict

filename = 'inputs/day23.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    input_list = [line.rstrip() for line in f]


def display_elves(elf_positions: dict):
    max_ex = max_ey = 0
    min_ex = min_ey = 0

    for this_elf in elf_positions:
        ex, ey = this_elf
        if ex > max_ex:
            max_ex = ex
        if ex < min_ex:
            min_ex = ex
        if ey > max_ey:
            max_ey = ey
        if ey < min_ey:
            min_ey = ey
    for this_y in range(min_ey, max_ey + 1):
        print_line = ''
        for this_x in range(min_ex, max_ex + 1):
            if (this_x, this_y) in elf_positions:
                print_line += '#'
            else:
                print_line += '.'
        print(print_line)
    print()


elves = defaultdict(str)
direction_order = 'NSWE'
for y, this_line in enumerate(input_list):
    for x, this_char in enumerate(this_line):
        if this_char == '#':
            elves[(x, y)] = ''


round_count = 1
while True:
    # A dictionary of proposed (x, y) coordinates elves want to move to. Elves will append
    # their current position to the list for the (x, y) they want to go to. That way we can
    # know how many elves want to move to each position.
    proposals = defaultdict(list)

    # Step 1: Each elf considers N, S, W, E in order and proposes a move
    for this_elf in elves:

        elf_x, elf_y = this_elf
        # Step 1a: Each elf checks whether there is an elf next to them
        needs_to_move = False
        for neighbor in [(elf_x-1, elf_y-1), (elf_x, elf_y-1), (elf_x+1, elf_y-1),
                         (elf_x-1, elf_y), (elf_x+1, elf_y),
                         (elf_x-1, elf_y+1), (elf_x, elf_y+1), (elf_x+1, elf_y+1)]:
            if neighbor in elves:
                needs_to_move = True
                break

        # Step 1b: If so, they propose a move
        if needs_to_move:
            # The first direction everyone will look in. At the end of this whole for loop
            # we'll update direction_order so that the correct direction is in the 0th position
            search_dir = direction_order[0]

            proposal = None
            p_count = 0
            while p_count < 4:
                if search_dir == 'N':
                    if not any(e in elves for e in [(elf_x-1, elf_y-1), (elf_x, elf_y-1), (elf_x+1, elf_y-1)]):
                        proposal = (elf_x, elf_y - 1)
                        break
                    else:
                        search_dir = 'S'
                        p_count += 1
                elif search_dir == 'S':
                    if not any(e in elves for e in [(elf_x-1, elf_y+1), (elf_x, elf_y+1), (elf_x+1, elf_y+1)]):
                        proposal = (elf_x, elf_y + 1)
                        break
                    else:
                        search_dir = 'W'
                        p_count += 1
                elif search_dir == 'W':
                    if not any(e in elves for e in [(elf_x-1, elf_y-1), (elf_x-1, elf_y), (elf_x-1, elf_y+1)]):
                        proposal = (elf_x - 1, elf_y)
                        break
                    else:
                        search_dir = 'E'
                        p_count += 1
                elif search_dir == 'E':
                    if not any(e in elves for e in [(elf_x+1, elf_y-1), (elf_x+1, elf_y), (elf_x+1, elf_y+1)]):
                        proposal = (elf_x+1, elf_y)
                        break
                    else:
                        search_dir = 'N'
                        p_count += 1
            if proposal is not None:
                proposals[proposal].append(this_elf)

    # Step 2: For each proposed move, if only one elf wants to go there, move them
    if len(proposals) == 0:
        # If there are no proposals, part 2 is complete
        break
    for this_proposal in proposals:
        elf_list = proposals[this_proposal]
        if len(elf_list) == 1:
            elves[this_proposal] = elves[elf_list[0]]
            del elves[elf_list[0]]

    # Rotate the direction order for next round
    direction_order = direction_order[1:] + direction_order[0]

    # Do part 1 stuff
    if round_count == 10:
        max_x = max_y = 0
        min_x = min_y = 0
        for this_elf in elves:
            ex, ey = this_elf
            if ex > max_x:
                max_x = ex
            if ex < min_x:
                min_x = ex
            if ey > max_y:
                max_y = ey
            if ey < min_y:
                min_y = ey

        width = max_x + 1 - min_x
        height = max_y + 1 - min_y
        area = width * height
        result = area - len(elves)
        print(f"Part 1: {result}")

    round_count += 1

print(f"Part 2: {round_count}")