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
'''
def levelorder(node):
    A = []
    s = -1
    e = -1
    A.append(node)
    s += 1
    e += 1
    while s <= e:
        curr = A[s]
        s += 1
        print(curr.data)
        if curr.left != None:
            A.append(curr.left)
            e += 1
        if curr.right != None:
            A.append(curr.right)
            e += 1
    return A
'''
def levelorder2(node):
    A = []
    s = -1
    e = -1
    A.append(node)
    s = 0
    e = 0
    while s <= e:
        curr = A[s]
        s += 1
        print(curr.data)
        if curr.left != None:
            A.append(curr.left)
            e += 1
        if curr.right != None:
            A.append(curr.right)
            e += 1
    return A



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
    ans = levelorder2(root)
    print(ans)