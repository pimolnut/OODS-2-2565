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
        a = Node(data)
        if self.root is None:
            self.root = a
            return "*"
        else:
            root = self.root
            s = ""
            while True:
                if data <= root.data:
                    if root.left is None:
                        root.left = a
                        s += "L*"
                        return s
                    else:
                        root = root.left
                        s += "L"
                else:
                    if root.right is None:
                        root.right = a
                        s += "R*"
                        return s
                    else:
                        root = root.right
                        s += "R"


t = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:
    print(t.insert(i))