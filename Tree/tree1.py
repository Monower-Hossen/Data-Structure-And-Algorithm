class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

# Assigning node values
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")
k = Node("K")
l = Node("L")

# Adding children to nodes
a.add_child(b)
a.add_child(c)
a.add_child(d)

b.add_child(e)
b.add_child(f)
b.add_child(g)

g.add_child(h)

d.add_child(k)
d.add_child(l)

# Printing children of A
print("Children of A are:")
for child in a.children:
    print(child.data)

# Printing children of D
print("Children of D are:")
for child in d.children:
    print(child.data)
