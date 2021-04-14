'''
Exercício parcial 03 [Árvore]
Dupla: Hélio Potelicki e Pedro Henrique Roweder 

'''


# ============================= Nó ============================= #
class Node:
    def __init__(self, data):
        self.data = data
        self.index = None
        self.left = None
        self.right = None

    def getIndex(self):
        return (self.index)

    def cal_index(self, count, tree):
        self.index = count
        value = tree.amount.get(count)

        if (value is None):
            tree.amount.update({count: self.data})
        else:
            tree.amount.update({count: (value + self.data)})

        if (self.left != None):
            count -= 1
            self.left.cal_index(count, tree)
            count += 1

        if (self.right != None):
            count += 1
            self.right.cal_index(count, tree)

    def init_index(self, tree):
        self.cal_index(0, tree)

    def print_node(self):
        ret = '<' + str(self.data)

        if (self.left != None):
            ret += self.left.print_node()

        if (self.right != None):
            ret += self.right.print_node()

        ret += '>'

        return ret


# ============================= Árvore ============================= #
class BinaryTree:
    def __init__(self, data=None, node=None):
        self.amount = {}

        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def getAmount(self):
        return (str(sorted(self.amount.items(),
                           key=lambda item: item[0]))[1:-1])

    def print_tree(self):
        if (not self.root):
            return ('<>')
        else:
            return (self.root.print_node())

    def index_dict(self):
        self.root.init_index(tree)


# ============================= Main ============================= #
tree = BinaryTree(5)
tree.root.left = Node(7)
tree.root.right = Node(3)
tree.root.right.left = Node(6)
tree.index_dict()

print(f'\nÁrvore: {tree.print_tree()}')
print(f'Contagem das folhas por índice: {tree.getAmount()}')