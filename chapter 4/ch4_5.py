class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def enqueue(self, i):
        self.items.append(i)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


inp = input("Enter Input (Normal, Mirror) : ").split(" ")
normal = Queue()
mirror = Stack()
mirrorItemBoom = Queue()
NormalBoom = 0
NormalFailed = 0
mirrorBoom = 0

for i in reversed(inp[1]):
    mirror.push(i)
    # print(mirror.items)
    if (mirror.size() >= 3) and ((mirror.items[-1] == mirror.items[-2] == mirror.items[-3])):
        mirrorItemBoom.enqueue(mirror.pop())
        mirror.pop()
        mirror.pop()
        mirrorBoom = mirrorBoom + 1
    # print(mirrorBoom)
    # print(mirrorItemBoom.items)

for j in inp[0]:
    normal.enqueue(j)
    # print(normal.items)
    if normal.size() >= 3 and normal.items[-1] == normal.items[-2] == normal.items[-3] and not mirrorItemBoom.isEmpty():
        x = normal.items.pop()
        normal.enqueue(mirrorItemBoom.dequeue())
        normal.enqueue(x)
        if normal.items[-1] == normal.items[-2] == normal.items[-3]:
            normal.items.pop()
            normal.items.pop()
            normal.items.pop()
            NormalFailed = NormalFailed + 1
    else:
        if normal.size() >= 3 and normal.items[-1] == normal.items[-2] == normal.items[-3]:
            normal.items.pop()
            normal.items.pop()
            normal.items.pop()
            NormalBoom = NormalBoom + 1

print("NORMAL :")
print(normal.size())
if normal.isEmpty():
    print('Empty')
else:
    print(''.join(reversed(normal.items)))
print(f'{NormalBoom} Explosive(s) ! ! ! (NORMAL)')
if NormalFailed != 0:
    print(f'Failed Interrupted {NormalFailed} Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(mirror.size())
if mirror.isEmpty():
    print("ytpmE")
else:
    print(''.join(reversed(mirror.items)))
print(f'(RORRIM) ! ! ! (s)evisolpxE {mirrorBoom}')