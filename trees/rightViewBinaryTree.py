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

def rightview(node):
    A = []
    s = -1
    e = -1
    A.append(node)
    A.append(None)
    s += 1
    e += 2
    while s < e:
        curr = A[s]
        s += 1
        if curr == None:
            A.append(None)
            e += 1
        else:
            if curr.left != None:
                A.append(curr.left)
                e += 1
            if curr.right != None:
                A.append(curr.right)
                e += 1
    
    n = len(A)
    print(A[0].data)
    for i in range(1,n):
        if A[i] == None:
            print(A[i-1].data)
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
    ans = rightview(root)
