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

def childrenSum(node):
    sumi = 0
    if node == None:
        return True
    if node.left == None and node.right == None:
        return True   
    else:
        if node.left != None:
            sumi += node.left.data
        if node.right != None:
            sumi += node.right.data
        if node.data == sumi and childrenSum(node.left) and childrenSum(node.right):
            return True
    return False


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
    ans = childrenSum(root)
    print(ans)
