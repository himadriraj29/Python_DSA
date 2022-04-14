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

def spiral(node):
    L2R = []
    R2L = []
    res = []
    L = 1
    L2R.append(node)
    while len(L2R)  != 0 or len(R2L) != 0:
        if L:
            for i in L2R:
                if i.left:
                    R2L.append(i.left)
                if i.right:
                    R2L.append(i.right)
                res.append(i.data)
            L = 0
            L2R.clear()
        else:
            for i in R2L:
                if i.left:
                    L2R.append(i.left)
                if i.right:
                    L2R.append(i.right)
            for i in range(len(R2L)-1,-1,-1):
                res.append(R2L[i].data)
            L = 1
            R2L.clear()

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
    ans = spiral(root)
    print(ans)
