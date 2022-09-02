class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[0]


people = Queue()
cashier1 = Queue()
cashier2 = Queue()
count_time_cashier1 = 0
count_time_cashier2 = 0
list = input("Enter people : ")

for x in list:
    people.enqueue(x)

for i in range(len(list)):
    if count_time_cashier1 == 3:
        cashier1.dequeue()
        count_time_cashier1 = 0

    if count_time_cashier2 == 2:
        cashier2.dequeue()
        count_time_cashier2 = 0

    if cashier1.size() < 5 and people.size() != 0:
        cashier1.enqueue(people.dequeue())
    elif cashier1.size() >= 5 and people.size() != 0:
        cashier2.enqueue(people.dequeue())

    if cashier1.size() != 0:
        count_time_cashier1 += 1
    if cashier2.size() != 0:
        count_time_cashier2 += 1

    print(i+1,people.items,cashier1.items,cashier2.items)

