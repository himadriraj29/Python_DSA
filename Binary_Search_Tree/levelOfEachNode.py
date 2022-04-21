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

def levelOfNode(node):
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
    disc = {}
    n = len(A)
    j = 0
    disc[j] = A[0].data
    print(A[0].data)
    for i in range(1,n-1):
        if A[i] == None:
            #print(A[i+1].data)
            j += 1
            while A[i] != None:
                disc[j] = A[i+1].data
                i += 1
            i -= 1
    return disc

if __name__ == "__main__":
    root = buildTree()
    #print(node)
    '''
    node = Node(1)
    node.left = Node(2)
    node.left.left = Node(8)
    node.left.right = Node(7)
    node.right = Node(3)
    '''
    #arr = []
    #ans = pairsum(root,3)
    ans = levelOfNode(root)
    print(ans)