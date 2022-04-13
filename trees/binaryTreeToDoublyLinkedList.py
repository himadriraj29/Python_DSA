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
    res = 0
    count = 0
    for i in range(0,n):
        count += 1
        if A[i] == None:
            res = max(count-1,res)
            count = 0
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
    ans = BTDL(root)
    print(ans)
