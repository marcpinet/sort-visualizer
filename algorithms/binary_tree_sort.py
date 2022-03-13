def sort(array: list[int]):
    """Binary Search Tree Sort"""
    final_return = []
    steps = []

    class BinSearchTreeNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None
            self.parent = None

        def insert_elem(self, node):
            if self.key > node.key:
                if self.left is None:
                    self.left = node
                    node.parent = self
                    yield array, [node.key]
                else:
                    yield from self.left.insert_elem(node)
            elif self.key <= node.key:
                if self.right is None:
                    self.right = node
                    node.parent = self
                    yield array, [node.key]
                else:
                    yield from self.right.insert_elem(node)

        def inorder_traversal(self):
            if self.left is not None:
                self.left.inorder_traversal()
            final_return.append(self.key)
            tmp = final_return.copy()
            tmp.extend([x for x in array if x not in tmp])
            steps.append(tmp)
            if self.right is not None:
                self.right.inorder_traversal()

    class BinSearchTree:
        def __init__(self):
            self.root = None

        def inorder_traversal(self):
            if self.root is not None:
                self.root.inorder_traversal()

        def add_val(self, key):
            new_node = BinSearchTreeNode(key)
            yield array, [key]
            
            if self.root is None:
                self.root = new_node
            else:
                yield from self.root.insert_elem(new_node)

    bst = BinSearchTree()
    for x in array:
        yield from bst.add_val(x)

    bst.inorder_traversal()
    
    i = 0
    for step in steps:
        yield array, [i]
        array = step
        i += 1

    yield final_return, []
