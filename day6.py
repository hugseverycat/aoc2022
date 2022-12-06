filename = 'inputs/day6.txt'
filename = 'inputs/test.txt'

with open(filename) as f:
    signal = f.readline()

buffer = ''
b_len = 4   # Part 1: 4; Part 2: 14

for i, c in enumerate(signal):
    buffer += c
    if len(buffer) == b_len:
        if len(set(buffer)) == b_len:
            marker = i + 1
            break
        else:
            buffer = buffer[1:]

print("Result:", marker)
