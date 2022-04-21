
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
class myNode:
    def __init__(self,k,v):
        self.k = k
        self.v = v
A[0] = myNode(3,56)
dis[-1] = A[0]
def buildTree():
    data = int(input())
    if data == -1:
        return None
    node = Node(data)
    node.left = buildTree()
    node.right = buildTree()
    return node

def levelOrder(node):
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
    for i in range(1,n-1):
        if A[i] == None:
            print(A[i+1].data)
    return A



def verticalNodeDistance(node,hd,disc):
    if node == None:
        return
    verticalNodeDistance(node.left,hd-1,disc)

    if(hd in disc.keys()):
        disc[hd] = disc[hd] + node.data
    else:
        disc[hd] = node.data
    
    verticalNodeDistance(node.right,hd+1,disc)

def verticalTraversal(node):
    disc = {}
    verticalNodeDistance(node,0,disc)
    for i,j in disc.items():
        print(i, ' = ',j, end = '  ')


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
    ans = verticalTraversal(root)
    #print(ans)