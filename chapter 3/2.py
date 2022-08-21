class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def ManageStack(s, list1, list2):
    if s[0] == 'A':
        list1.push(s[1])
        print("Add =", s[1])
    elif s[0] == 'P':
        if list1.isEmpty():
            print("-1")
        else:
            print("Pop =", list1.pop())
    elif s[0] == 'D':
        if list1.isEmpty():
            print("-1")
        else:
            for i in range(list1.size() - 1, -1, -1):
                if s[1] == list1.items[i]:
                    list2.push(list1.items[i])
            while not list2.isEmpty():
                list1.items.remove(s[1])
                print("Delete = " + list2.pop())
    elif s[0] == 'LD':
        if list1.isEmpty():
            print("-1")
        else:
            for i in range(list1.size() - 1, -1, -1):
                if int(s[1]) > int(list1.items[i]):
                    list2.push(list1.items[i])
            while not list2.isEmpty():
                popInt = list2.items.pop(0)
                list1.items.remove(popInt)
                print("Delete = " + popInt + " Because " + popInt + " is less than " + s[1])
    elif s[0] == 'MD':
        if list1.isEmpty():
            print("-1")
        else:
            for i in range(list1.size() - 1, -1, -1):
                if int(s[1]) < int(list1.items[i]):
                    list2.push(list1.items[i])
            while not list2.isEmpty():
                popInt = list2.items.pop(0)
                list1.items.remove(popInt)
                print("Delete = " + popInt + " Because " + popInt + " is more than " + s[1])

list1 = Stack()
list2 = Stack()
inp = input("Enter Input : ").split(",")
for e in inp:
    if len(e) > 1:
        s = e.split()
    else:
        s = e
    ManageStack(s, list1, list2)
print("Value in Stack =", str(list1.items).replace("\'", ""))