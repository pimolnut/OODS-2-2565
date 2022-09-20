class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.size == 0

    def append(self, value):
        # cur = Node(value)
        if self.head == None:
            self.head = Node(value)
            self.size += 1
        else:
            t = self.head
            for i in range(0, self.size-1):
                t = t.next
            cur = Node(value)
            t.next = cur
            self.size += 1

    def addHead(self, item):
        if self.isEmpty():
            cur = Node(item)
            self.head = cur
            self.size += 1
        else:
            cur = Node(item)
            cur.next = self.head
            self.head = cur
            self.size += 1

    def search(self, item):
        if self.index(item) >= 0:
            return "Found"
        else:
            return "Not Found"

    def index(self, item):
        p = self.head
        for i in range(self.size):
            if p.value == item:
                return i
            p = p.next
        return -1

    def Size(self):
        return self.size

    def pop(self, pos):
        if pos < 0 or pos >= self.size:
            return "Out of Range"
        elif pos == 0 and self.size > 0:
            self.head = self.head.next
            self.size -= 1
            return "Success"
        else:
            cur = self.head
            for i in range(0,pos-1):
                cur = cur.next
            cur.next = cur.next.next
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
        print("{0} {1}".format(L.search(i[3:]), i[3:]),end=" ")
        if L.search(i[3:]) == 'Found':
            print(f"in {L}")
        elif L.search(i[3:]) == 'Not Found' and L.isEmpty():
            print("in Empty")
        elif L.search(i[3:]) == 'Not Found' and L.size != 0:
            print(f"in {L}")
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.Size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)