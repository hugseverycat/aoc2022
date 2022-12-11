filename = 'inputs/day11.txt'
#filename = 'inputs/test.txt'

with open(filename) as f:
    lines = [line.rstrip() for line in f]

lines.append('')

"""
Monkey 0:
  Starting items: 54, 53
  Operation: new = old * 3
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 6
"""



#print(f"{m_items}\n{m_operation}\n{m_test}\n{m_partners}")


class Monkey:
    def __init__(self, input_data):
        m_id = input_data[0].split(' ')
        self.id = int(m_id[1][0])
        self.items = [int(i) for i in input_data[1][18:].split(',')]
        #print(self.items)
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
        try:
            self.true_monkey = m_list[self.partner_ids[0]]
            self.false_monkey = m_list[self.partner_ids[1]]
            #print(self.true_monkey)
        except IndexError:
            print(self.items)
            print(self.partner_ids)
            print(m_list)
            raise

    def increase_worry(self, worry_level):
        if self.operand == "old":
            o = worry_level
        else:
            o = int(self.operand)

        if self.op == '*':
            #print(f"    Worry level is multiplied by {o} to {worry_level * o}")
            return worry_level * o
        else:
            #print(f"    Worry level increases by {o} to {worry_level + o}")
            return worry_level + o

    def handle_items(self):
        for this_item in self.items:
            self.inspect_count += 1
            #print(f"  Monkey inspects an item with a worry level of {this_item}")
            this_item = self.increase_worry(this_item)//3
            #print(f"    Monkey gets bored with item. Worry level is divided by 3 to {this_item}")
            if this_item//self.test == this_item/self.test:
                #print(f"    Current worry level *IS* divisible by {self.test}.")
                self.true_monkey.receive(this_item)
            else:
                #print(f"    Current worry level *IS NOT* divisible by {self.test}.")
                self.false_monkey.receive(this_item)
        self.items = []
        #print()

    def receive(self, new_item):
        #print(f"    Item with worry level {new_item} is thrown to monkey {self.id}")
        self.items.append(new_item)


monkey_list = []
temp_monkeys = [lines[n*7:(n+1) * 7] for n in range(0, len(lines)//7)]
#print(temp_monkeys)
for this_monkey in temp_monkeys:
    monkey_list.append(Monkey(this_monkey))

for this_monkey in monkey_list:
    this_monkey.set_partners(monkey_list)

for round in range(1, 10001):
    for this_monkey in monkey_list:
        #print(f"Monkey {this_monkey.id}:")
        this_monkey.handle_items()
    #print(f"After round {round}, the monkeys are holding items with these worry levels:")
    """for this_monkey in monkey_list:
        this_monkey.print_items()
    print()"""

inspect = sorted([m.inspect_count for m in monkey_list], reverse=True)
print(inspect[0] * inspect[1])
