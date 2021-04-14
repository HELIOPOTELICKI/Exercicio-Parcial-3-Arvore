# ============================= Nó ============================= #
class Node:
    def __init__(self, data):
        self.data = data
        self.index = None
        self.left = None
        self.right = None

    def getIndex(self):
        return (self.index)

    def cal_index(self, count):
        self.index = count

        if (self.left != None):
            count -= 1
            self.left.cal_index(count)
            count += 1

        if (self.right != None):
            count += 1
            self.right.cal_index(count)

    def init_index(self):
        self.cal_index(0)

    def print_node(self):
        ret = '<' + str(self.data)

        if (self.left != None):
            ret += self.left.print_node()

        if (self.right != None):
            ret += self.right.print_node()

        ret += '>'

        return ret

    def sumLeaves(self):
        return 'not implemented dude'


# ============================= Árvore ============================= #
class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def print_tree(self):
        if (not self.root):
            return ('<>')
        else:
            return (self.root.print_node())

    def index_dict(self):
        self.root.init_index()
        return (Node.getIndex(self.root))

    def hLeaves(self):
        return (self.root.sumLeaves())


# ============================= Main ============================= #
tree = BinaryTree(5)
tree.root.left = Node(7)
tree.root.right = Node(3)
tree.root.right.left = Node(6)

tree.index_dict()
print('\n' + tree.print_tree())

print(tree.root.getIndex())  #  0
print(tree.root.left.getIndex())  # -1
print(tree.root.right.getIndex())  #  1
print(tree.root.right.left.getIndex())  #  0

#print('\n' + tree.hLeaves())
