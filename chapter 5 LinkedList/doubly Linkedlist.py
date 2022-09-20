class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
            self.size += 1
            return
        self.size += 1
        cur = self.head
        while cur.next != None:
            cur = cur.next
        newNode = Node(item)
        newNode.previous = cur
        cur.next = newNode
        self.tail = newNode

    def addHead(self, item):
        if self.isEmpty():
            self.head = self.tail = Node(item)
            self.size += 1
            return
        self.size += 1
        newNode = Node(item)
        if self.size == 1:
            newNode.next = self.tail
            self.tail.previous = newNode
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode

    def insert(self, pos, item):
        newNode = Node(item)
        if pos > self.size or pos == self.size:
            if self.isEmpty():
                self.head = self.tail = newNode
                self.size += 1
                return
            else:
                self.tail.next = newNode
                newNode.previous = self.tail
                self.tail = newNode
                self.size += 1
                return
        if pos < -(self.size) or pos == 0:
            if self.isEmpty():
                self.head = self.tail = newNode
                self.size += 1
                return
            else:
                newNode.next = self.head
                self.head.previous = newNode
                self.head = newNode
                self.size += 1
                return

        if pos > 0 and pos < self.size:
            i = 0
            cur = self.head
            while i != pos - 1:
                cur = cur.next
                i += 1
            cur.next.previous = newNode
            newNode.next = cur.next
            newNode.previous = cur
            cur.next = newNode
            self.size += 1
            return
        if pos < 0 and pos > -(self.size):
            i = 0
            cur = self.tail
            while i != pos + 1:
                cur = cur.previous
                i -= 1
            cur.previous.next = newNode
            newNode.previous = cur.previous
            newNode.next = cur
            cur.previous = newNode
            self.size += 1
            return

    def search(self, item):
        cur = self.head
        while cur.value != item:
            cur = cur.next
            if cur == None:
                return "Not Found"
        return "Found"

    def index(self, item):
        i = 0
        cur = self.head
        if cur.value == item:
            return i
        while cur.value != item:
            cur = cur.next
            i += 1
            if i == self.size:
                return -1
            if cur.value == item:
                return i

    def size(self):
        return self.size

    def pop(self, pos):

        if (pos >= self.size) or (pos < 0):
            return "Out of Range"

        if pos == 0 and self.size == 1:
            self.head = None
            self.size -= 1
            return "Success"
        elif pos == 0 and not self.isEmpty():
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1
            return "Success"
        elif pos == 0 and self.isEmpty():
            return "Out of Range"

        cur = self.head
        count = 0
        while count != pos - 1:
            cur = cur.next
            count += 1
        if pos + 1 == self.size:
            cur.next = None
            self.tail = self.tail.previous
            return "Success"
        cur.next = cur.next.next
        cur.next.previous = cur
        self.size -= 1
        return "Success"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size, L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())