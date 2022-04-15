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

def insert(node,key):
    if node == None:
        node = Node(key)
    elif node.data > key:
        return insert(node.left,key)
    elif node.data < key:
        return insert(node.right,key)
    return node.data
    #return False

if __name__ == "__main__":
    root = buildTree()
    #print(root)
    '''
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(8)
    root.left.right = Node(7)
    root.right = Node(3)
    '''
    ans = insert(root,4)
    print(ans)

