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

def height(node):
    if node == None:
        return 0
    lh = height(node.left)
    rh = height(node.right)
    return max(lh,rh)+1

#naive approach
def diameter(node):
    if node == None:
        return 0
    d = 1 + height(node.left) + height(node.right)
    dl = 1 + diameter(node.left)
    dr = 1 + diameter(node.right)
    return max(d,max(dl,dr))

#optimised approach using height as diameter by precomputing height of every node
def height_dia(node):
    res = 0
    if node == None:
        return 0
    lh = height_dia(node.left)
    rh = height_dia(node.right)
    res = max(res, lh+rh+1)
    #return 1 + max(lh,rh)
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
    ans = height_dia(root)
    print(ans)
