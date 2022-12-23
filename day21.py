import re

filename = 'inputs/day21.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    input_list = [line.rstrip() for line in f]

monkeys = {}
for this_line in input_list:
    this_monkey = this_line[0:4]
    try:
        monkey_command = int(this_line[6:])
    except ValueError:
        monkey_command = (this_line[6:])
    monkeys[this_monkey] = monkey_command


def get_monkey_value(monk: str, all_monks: dict):
    monkey_value = all_monks[monk]
    if type(monkey_value) == int:
        return monkey_value

    monkey_a, monkey_b = re.findall("[a-z]{4}", monkey_value)
    monkey_operation = monkey_value[5]

    all_monks[monkey_a] = get_monkey_value(monkey_a, all_monks)
    all_monks[monkey_b] = get_monkey_value(monkey_b, all_monks)

    if monkey_operation == '+':
        monkey_value = all_monks[monkey_a] + all_monks[monkey_b]
    elif monkey_operation == '*':
        monkey_value = all_monks[monkey_a] * all_monks[monkey_b]
    elif monkey_operation == '/':
        monkey_value = all_monks[monkey_a] // all_monks[monkey_b]
    elif monkey_operation == '-':
        monkey_value = all_monks[monkey_a] - all_monks[monkey_b]
    else:
        print(f"Invalid monkey operation found: {monkey_operation}")
        raise ValueError

    all_monks[monk] = monkey_value
    return monkey_value


def get_human_value(monk: str, all_monks: dict):
    pass
    # assume we start with lvcv: snlt + humn
    # (test data: ptdq: humn - dvpt)

    equation = '(lycv - snlt)'
    

print(get_monkey_value('root', monkeys))
