class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


inp = input('Enter Infix : ')
S = Stack()
opdict = {'(': 0,
          '+': 1,
          '-': 1,
          '*': 2,
          '/': 2,
          '^': 3 }

print('Postfix : ', end='')
for i in inp:
    if i.isalpha():
        print(i,end='')
    else:
        if i == '(':
            S.push(i)
        elif i == ')':
            while S.peek() != '(':
                print(S.pop(),end='')
            S.pop()
        elif S.isEmpty() or opdict[i] > opdict[S.peek()]:
            S.push(i)
        else:
            while not S.isEmpty() and S.peek() != '(' and opdict[S.peek()] >= opdict[i]:
                print(S.pop(),end='')
            S.push(i)
while not S.isEmpty():
    print(S.pop(), end='')
print()