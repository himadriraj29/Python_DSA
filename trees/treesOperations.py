class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def buildTree():
    data = int(input())
    if data == -1:
        return None
    node = Node(data)
    node.left = buildTree()
    node.right = buildTree()
    return node

def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)

def height(node,h):
    if node == None:
        return h
    lh = height(node.left,h)
    rh = height(node.right,h)
    h = max(lh,rh)
    return h+1.
    

if __name__ == "__main__":
    #root = buildTree()
    #print(root)
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(8)
    root.left.right = Node(7)
    root.right = Node(3)
    inorder(root)



