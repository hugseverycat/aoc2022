filename = 'inputs/day6.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    signal = f.readline()

buffer = ''
for i, c in enumerate(signal):
    buffer += c
    if len(buffer) == 14:           # Switch to 4 for part 1
        if len(set(buffer)) == 14:  # Switch to 4 for part 1
            marker = i + 1
            break
        else:
            buffer = buffer[1:]

print("Result:", marker)
