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

def floorBST(node,key):
    if node == None:
        return None
    res = 0
    while node != None:
        if node == key:
            return key
        if node.data > key:
            node = node.left
        else:
            res = node
            node = node.right
    return res

    

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
    ans = floorBST(root,4)
    print(ans.data)

