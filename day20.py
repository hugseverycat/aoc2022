from collections import deque

filename = 'inputs/day20.txt'
#filename = 'inputs/test.txt'

decryption_key = 811589153

with open(filename) as f:
    # value_list will remain unchanged -- this is how we keep track of the initial order
    value_list = [int(line) * decryption_key for line in f]
    #  For part one remove multiplication by decryption key

total_values = len(value_list)

# mixed_values is the list that will be changing. deque because it'll rotate
mixed_values = deque(value_list.copy())

# current_index_list will change in the same way as mixed list
# it allows us to locate items from value_list by index
current_index_list = deque([i for i in range(total_values)])

for counter in range(10):  # Only once for part 1
    for i, v in enumerate(value_list):
        # Look up the current (mixed) index of the i-th value in value_list
        current_index = current_index_list.index(i)

        # remove that index from mixed values (current index list always mirrors)
        del mixed_values[current_index]
        del current_index_list[current_index]

        # rotate (-1 to reverse the rotation; by default deque moves the opposite way we want)
        mixed_values.rotate(v * -1)
        current_index_list.rotate(v * -1)

        # insert the deleted item back at the same index
        # because the list has rotated it'll be where we want
        mixed_values.insert(current_index, v)
        current_index_list.insert(current_index, i)

value_1 = mixed_values[(mixed_values.index(0) + 1000) % total_values]
value_2 = mixed_values[(mixed_values.index(0) + 2000) % total_values]
value_3 = mixed_values[(mixed_values.index(0) + 3000) % total_values]

print(f"Part 1: {value_1 + value_2 + value_3}")
