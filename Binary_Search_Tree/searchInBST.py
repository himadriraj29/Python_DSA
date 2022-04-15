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

def searchBST(node,key):
    if node == None:
        return False
    elif node.data == key:
        return True
    elif node.data > key:
        return searchBST(node.left,key)
    elif node.data < key:
        return searchBST(node.right,key)
    
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
    ans = searchBST(root,3)
    print(ans)

