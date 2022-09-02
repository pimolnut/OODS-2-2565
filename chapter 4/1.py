class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

q = Queue()
queue_pop = Queue()
m = input("Enter Input : ").split(",")
queue = []
list_d = []
for x in m:
    queue.extend(x.split())
check = 1
for i in range(len(queue)):
    if 'E' == queue[i]:
        check=1
        i += 1
        if queue[i] == '0':
            print("Empty")
        else:
            q.enqueue(queue[i])
            join = ", ".join(q.items)
            print(join)
    if 'D' == queue[i]:
        list_d.append(queue[i])
        # print(len(list_d))
        if not q.isEmpty():
            check = 1
            item = q.dequeue()
            queue_pop.enqueue(item)
            join1 = ", ".join(q.items)
            if q.size() != 0:
                print(f"{item} <- {join1}")
            else:
                print(f'{item} <- Empty')
        elif q.isEmpty():
            if check == 1 :
                print("Empty")
                check = 0



join3 = ", ".join(queue_pop.items)
join4 = ", ".join(q.items)
if queue_pop.isEmpty() and q.isEmpty():
    print("Empty : Empty")
elif not q.isEmpty() and not queue_pop.isEmpty():
    print(f"{join3} : {join4}")
elif not queue_pop.isEmpty() and q.isEmpty():
    print(f"{join3} : Empty")
else:
    print(f"Empty : {join4}")


