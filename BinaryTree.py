#============================= Nó =============================#
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_node(self):
        ret = '<' + str(self.data)

        if (self.left != None):
            ret += self.left.print_node()

        if (self.right != None):
            ret += self.right.print_node()

        ret += '>'

        return ret


#============================= Árvore =============================#
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


tree = BinaryTree(5)
tree.root.left = Node(7)
tree.root.right = Node(3)
tree.root.right.left = Node(6)

print('\n' + tree.print_tree())