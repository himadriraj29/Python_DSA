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

#approach-1 : naive approach
#find mini of right subtree
#find maxi of left sub tree
#node should be greater than max and smaller than minimum
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

#approach-2 : better approach
#pass a range for every node
#for root range is -inf to +inf
#for left child we change upper bound 
#for right we change lower bound
def checkBST_2(node,mini,maxi):
    if node == None:
        return True
    return node.data < maxi and node.data > mini and checkBST_2(node.left,mini,node.data) and checkBST_2(node.right,node.data,maxi)

#approach-3: best approach
#we do the inorder traversal of tree
#and check if the previous node is smaller or  not
prev = float('-inf')
def checkBST_3(node):
    global prev 
    #prev = None
    if node == None:
        return True
   # node = node.left
    if checkBST_3(node.left) == False:
        return False
    if node.data <= prev:
        return False
    prev = node.data
    return checkBST_3(node.right)


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
    mini = float('-inf')
    maxi = float('inf')
    #ans = checkBST_2(root,mini,maxi)
    ans = checkBST_3(root)
    print(ans[0].data,ans[1].data)