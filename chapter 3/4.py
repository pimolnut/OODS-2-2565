class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

inp = input('Enter Input : ').split(',')
S = Stack()
stack = []
for i in range(len(inp)):
    if inp[i] == 'B':
        k = 0
        count = 0
        for j in range(S.size()):
            x = int(S.pop())
            if k < x:
                count += 1
                k = x
        print(count)
        for m in range(len(stack)):
            S.push(stack[m])
    else:
        a = inp[i].split(' ')
        S.push(a[1])
        stack.append(a[1])