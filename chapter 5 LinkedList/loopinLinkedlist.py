class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0
        self.count = 0

    def append(self, item):
        if self.isEmpty():
            self.head = Node(item)
            self.size += 1
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(item)
        self.size += 1

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        Str = self.head.data
        cur = self.head
        i = 0
        while cur.next != None:
            if i < self.size:
                Str += "->"
            cur = cur.next
            Str += cur.data
            i += 1
        return Str

    def set_next(self, i1, i2):
        if self.isEmpty():
            return "Error! {list is empty}"
        if i1 > self.size - 1:
            return "Error! {index not in length}: " + str(i1)
        if i2 > self.size - 1:
            self.append(str(i2))
            return "index not in length, append : " + str(i2)

        if i1 < i2:
            i = 0
            cur = self.head
            cur1 = self.head
            while i < i2:
                if i < i1:
                    cur = cur.next
                cur1 = cur1.next
                i += 1
            cur.next = cur1
            return f"Set node.next complete!, index:value = {i1}:{cur.data} -> {i2}:{cur1.data}"

        if i1 > i2:
            self.count += 1
            i = 0
            cur = self.head
            cur1 = self.head
            while i < i1:
                if i < i2:
                    cur1 = cur1.next
                cur = cur.next
                i += 1
            return f"Set node.next complete!, index:value = {i1}:{cur.data} -> {i2}:{cur1.data}"
        if i1 == i2:
            self.count += 1
            i = 0
            cur = self.head
            while i < i1:
                cur = cur.next
                i += 1
            return f"Set node.next complete!, index:value = {i1}:{cur.data} -> {i2}:{cur.data}"

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0


L = LinkedList()
inp = input("Enter input : ").split(",")
for i in inp:
    if i[0] == "A":
        L.append(i[2:])
        print(L)
    elif i[0] == "S":
        print(L.set_next(int(i[2]), int(i[4])))

if L.count > 0:
    print("Found Loop")
else:
    print("No Loop")
    print(L)