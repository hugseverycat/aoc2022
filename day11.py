filename = 'inputs/day11.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]

part = 2
if part == 1:
    rounds = 20
else:
    rounds = 10000

group = [lines[n*7:n*7 + 7] for n in range((len(lines)+1)//7)]
monkeys = []

for g in group:
    new_monkey = {
        'items': [int(i) for i in g[1][18:].split(', ')],
        'operation': g[2].split(' ')[-2],
        'operand': g[2].split(' ')[-1],
        'div_test': int(g[3].split(' ')[-1]),
        'true_monkey': int(g[4].split(' ')[-1]),
        'false_monkey': int(g[5].split(' ')[-1]),
        'inspect_count': 0
    }
    monkeys.append(new_monkey)

# For part 2, we need to keep the worry level down. One way we
# can do this is by not caring about the actual worry level, but whether
# it is divisible by the test number. Since each monkey's test number is
# a prime, we can multiply all the primes together to get a common denominator.
# Then in part 2 we can modulo the worry level by the common denominator
# to get a smaller number that behaves the same way as the larger number
# with regard to divisibility.

common_denom = 1
for this_monkey in monkeys:
    common_denom *= this_monkey['div_test']

for _ in range(rounds):
    for this_monkey in monkeys:
        for this_item in this_monkey['items']:
            this_monkey['inspect_count'] += 1

            # Perform the operation
            if this_monkey['operation'] == '+':
                if this_monkey['operand'] == "old":
                    worry_level = this_item + this_item
                else:
                    worry_level = this_item + int(this_monkey['operand'])
            else:
                if this_monkey['operand'] == "old":
                    worry_level = this_item * this_item
                else:
                    worry_level = this_item * int(this_monkey['operand'])

            # Reduce worry level
            if part == 1:
                worry_level = worry_level//3
            else:
                worry_level = worry_level % common_denom

            # Pass item to next monkey
            if worry_level % this_monkey['div_test'] == 0:
                pass_monkey = this_monkey['true_monkey']
            else:
                pass_monkey = this_monkey['false_monkey']
            monkeys[pass_monkey]['items'].append(worry_level)

        # This monkey has passed all items
        this_monkey['items'] = []

# Calculate monkey business
inspections = sorted([m['inspect_count'] for m in monkeys], reverse=True)
print(f"Part {part}: {inspections[0] * inspections[1]}")
