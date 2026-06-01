class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class InfectionTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root

        print("   " * level + "|- " + str(node.data))

        for child in node.children:
            self.print_tree(child, level + 1)