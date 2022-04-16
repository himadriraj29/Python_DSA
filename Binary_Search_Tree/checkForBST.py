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
    
def mini(node):
    if node == None:
        return float('-inf')
    res = node.data
    lres = mini(node.left)
    rres = mini(node.right)
    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res

def maxi(node):
    if node == None:
        return float('inf')
    res = node.data
    lres = maxi(node.left)
    rres = maxi(node.right)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res

def checkBST_1(node):
    if node == None:
        return True
    if node.left != None and maxi(node.left) > node.data:
        return False
    if node.right != None and mini(node.right) < node.data:
        return False
    if checkBST_1(node.left) == False or checkBST_1(node.right) == False:
        return False
    return True

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
    ans = checkBST_1(root)
    print(ans)