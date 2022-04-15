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

def inorderSuccessor(node):
    curr = node.right
    if curr != None and curr.left != None:
        curr = curr.left
    return curr

def deletion(node,key):
    if node == None:
        return node
    if node.data > key:
        node.left = deletion(node.left,key)
    elif node.data < key:
        node.right = deletion(node.right,key)
    else:
        if node.left == None:
            return node.right
        elif node.right == None:
            return node.left
        else:
            succ = inorderSuccessor(node)
            root.data = succ.data
            root.right = deletion(root.right,succ.data)
    return node
    

            
    
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
    ans = deletion(root,1)
    print(ans.data)
    print(ans.left.data)

