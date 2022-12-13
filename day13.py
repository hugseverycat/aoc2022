filename = 'inputs/day13.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]


def compare_int(left: int, right: int):
    if left < right:
        return True
    if left > right:
        return False
    if left == right:
        return None


def compare_list(left: list, right: list):
    l_len = len(left)
    r_len = len(right)
    i = 0
    while True:
        # Check if we've reached the end of left or right
        if i == l_len and i == r_len:
            # We've reached the end of left and right and their length is the same
            return None
        elif i == l_len:
            # We've reached the end of left and left is shorter
            return True
        elif i == r_len:
            # We've reached the end of right and right is shorter
            return False

        # left and right both have more items to compare
        left_item = left[i]
        right_item = right[i]

        if isinstance(left_item, int) and isinstance(right_item, int):
            in_order = compare_int(left_item, right_item)
        elif isinstance(left_item, int):
            # Convert left item into a list and compare lists
            in_order = compare_list([left_item], right_item)
        elif isinstance(right_item, int):
            in_order = compare_list(left_item, [right_item])
        else:  # They are both lists, now compare them
            in_order = compare_list(left_item, right_item)

        if in_order is not None:
            return in_order

        i += 1


def bubble_sort(packets: list):
    num_packets = len(packets)

    for i in range(num_packets):
        for j in range(0, num_packets - i - 1):
            in_order = compare_list(packets[j], packets[j + 1])
            # in_order can be None if the packets are equivalent
            if in_order == False:
                packets[j], packets[j + 1] = packets[j + 1], packets[j]
    return packets


def solve_1(input_list: list):
    pairs = []
    temp_pair = []
    for this_line in input_list:
        if this_line == '':
            pairs.append(temp_pair)
            temp_pair = []
        else:
            temp_pair.append(eval(this_line))

    pairs.append(temp_pair)

    index_sum = 0
    for i, p in enumerate(pairs):
        in_order = compare_list(p[0], p[1])
        if in_order:
            index_sum += i + 1

    return index_sum


def solve_2(input_list: list):
    packet_list = []
    for this_line in input_list:
        if this_line == '':
            continue
        else:
            packet_list.append(eval(this_line))
    divider_1 = [[2]]
    divider_2 = [[6]]
    packet_list.append(divider_1)
    packet_list.append(divider_2)

    packet_list = bubble_sort(packet_list)
    return (packet_list.index(divider_1) + 1) * (packet_list.index(divider_2) + 1)


print(f"Part 1: {solve_1(lines)}")
print(f"Part 2: {solve_2(lines)}")
