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

def BTDL(node):
    prev = Node(None)
    head = Node(None)
    if node == None:
        return node
    else:
        head = BTDL(node.left)
        if prev == None:
            head = node
        else:
            node.left = prev
            prev.right = node
        prev = node
        BTDL(node.right)
    return head

def btdl(node):
    prev = Node(None)
    head = Node(None)
    if node == None:
        return node
    else:
        head = btdl(node.left)
        if prev == None:
            head = node
        else:
            node.left = prev
            prev.right = node
        prev = node
        btdl(node.right)
    return head





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
    ans = btdl(root)
    print(ans)


