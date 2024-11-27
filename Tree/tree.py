class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child (self , child):
        child.parent = self
        self.children.append(child)

def print_tree (self)
    print(self.data)
    for child in self.children:
        child.print_tree

def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode('Laptops')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))

    cellphone = TreeNode("cell phone")
    cellphone.add_child(TreeNode('I-Phone'))
    cellphone.add_child(TreeNode('vivo'))
    cellphone.add_child(TreeNode('google pixel'))

    tv = TreeNode("TV")
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('Lg'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

if __name__ = '__main__':
    build_product_tree ()
