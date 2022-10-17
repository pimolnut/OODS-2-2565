class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            node = self.root
            while True:
                if data < node.data:
                    if node.left is None:
                        node.left = Node(data)
                        break
                    node = node.left
                else:
                    if node.right is None:
                        node.right = Node(data)
                        break
                    node = node.right
        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def DataMin(self):
        cur = self.root
        while cur.left is not None:
            cur = cur.left
        return cur.data

    def DataMax(self):
        cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur.data


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')
print('Min :', T.DataMin())
print('Max :', T.DataMax())