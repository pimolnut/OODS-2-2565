class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, node):
        self.root = node

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        elif self.root is not None:
            p = self.root
            while p is not None:
                if data >= p.data:
                    if p.right is None:
                        p.right = Node(data)
                        break
                    p = p.right

                elif data < p.data:
                    if p.left is None:
                        p.left = Node(data)
                        break
                    p = p.left

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return 'Node : ' + str(self.data)


inp, check = input('Enter Input : ').split('/')
inpLis = [int(e) for e in inp.split()]
total = 0
for i in range(len(inpLis) - 1, -1, -1):
    total += inpLis[i]
    s = ''
    s += 'data : '
    s += str(inpLis[i])
    node = Node(inpLis[i])
    if (2 * i) + 1 < len(inpLis):
        s += ' child 1 : '
        s += str(inpLis[(2 * i) + 1])
        node.left = inpLis[(2 * i) + 1]
    if (2 * i) + 2 < len(inpLis):
        s += ' child 1 : '
        s += str(inpLis[(2 * i) + 2])
        node.right = inpLis[(2 * i) + 2]
    if node.left is not None:
        node.data += node.left.data
    if node.right is not None:
        node.data += node.right.data
    inpLis[i] = node
check = check.split(',')
print(total)
for i in check:
    x, y = [int(r) for r in i.split(' ')]
    if inpLis[x].data < inpLis[y].data:
        print(str(x) + '<' + str(y))
    if inpLis[x].data > inpLis[y].data:
        print(str(x) + '>' + str(y))
    if inpLis[x].data == inpLis[y].data:
        print(str(x) + '=' + str(y))