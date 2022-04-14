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

#naive approach
def countNode(node):
    res = 0
    if node == None:
        return 0
    lc = countNode(node.left)
    rc = countNode(node.right)
    res = lc+rc+1
    #return 1 + max(lh,rh)
    return res

#optimized approach
def countNodeEff(node):
    lh = 0
    rh = 0
    curr = Node(node)
    while curr != None:
        lh += 1
        curr = curr.left

    curr = node
    while curr != None:
        rh += 1
        curr = curr.right

    if lh == rh:
        return pow(2,lh) - 1
    return 1 + countNodeEff(node.left) + countNodeEff(node.right)


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
    ans = countNodeEff(root)
    print(ans)
