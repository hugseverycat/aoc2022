filename = 'inputs/day11.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]

lines.append('')

class Monkey:
    def __init__(self, input_data):
        m_id = input_data[0].split(' ')
        self.id = int(m_id[1][0])
        self.items = [int(i) for i in input_data[1][18:].split(',')]
        m_operation = [m.strip() for m in input_data[2].split(' ')]
        m_test = [m.strip() for m in input_data[3].split(' ')]
        self.partner_ids = [int(input_data[4][-1]), int(input_data[5][-1])]

        self.op, self.operand = [m_operation[6], m_operation[7]]
        self.test = int(m_test[-1])
        self.true_monkey = None
        self.false_monkey = None
        self.inspect_count = 0

    def print_items(self):
        print(f"Monkey {self.id}: {''.join([str(s) + ', ' for s in self.items])}")

    def set_partners(self, m_list):
        self.true_monkey = m_list[self.partner_ids[0]]
        self.false_monkey = m_list[self.partner_ids[1]]

    def increase_worry(self, worry_level, c_len):
        if self.operand == "old":
            o = worry_level
        else:
            o = int(self.operand)

        if self.op == '*':
            worry_level = worry_level * o
        else:
            worry_level = worry_level + o

        return (worry_level % c_len)
    def handle_items(self, c_len):
        for this_item in self.items:
            self.inspect_count += 1
            #this_item = self.increase_worry(this_item)//3
            this_item = self.increase_worry(this_item, c_len)
            if this_item//self.test == this_item/self.test:
                self.true_monkey.receive(this_item)
            else:
                self.false_monkey.receive(this_item)
        self.items = []

    def receive(self, new_item):
        self.items.append(new_item)


monkey_list = []
temp_monkeys = [lines[n*7:(n+1) * 7] for n in range(0, len(lines)//7)]

for this_monkey in temp_monkeys:
    monkey_list.append(Monkey(this_monkey))

for this_monkey in monkey_list:
    this_monkey.set_partners(monkey_list)

cycle_length = 1
for m in monkey_list:
    cycle_length *= m.test
print(cycle_length)

for _ in range(10000):
    for m in monkey_list:
        m.handle_items(cycle_length)

counts = sorted([s.inspect_count for s in monkey_list], reverse=True)
print(counts[0] * counts[1])
print(len(monkey_list))
