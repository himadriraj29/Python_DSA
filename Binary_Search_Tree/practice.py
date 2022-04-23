# Definition for a  binary tree node
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

def inorder(node,arr):
    if node == None:
        return
    inorder(node.left,arr)
    arr.append(node.data)
    inorder(node.right,arr)
    return arr
 
	# @param node : root node of tree
	# @return a list of integers
#recovering binary tree
def recoverTree(node):
    first = 0
    second = 0
    ans = []
    arr1 = inorder(node,arr) 
    n = len(arr1)
    for i in range(1,n):
        count = 0
        if arr1[i-1] > arr1[i]:
            first = arr1[i-1]
            break
        count += 1
    for i in range(count,n):
        if arr1[i] < arr1[i-1]:
            second = arr1[i]
    #first,second = second,first
    ans.append(first)
    ans.append(second)
    return ans

#finding lca
def path(node,p,key):
    if node == None:
        return False
    p.append(node.data)
    if node.data == key:
        return True
    if (node.left != None and path(node.left,p,key)) or (node.right != None and path(node.right,p,key)):
        return True
    p.pop()
    return False

def lca(node,n1,n2):
    p1 = []
    p2 = []
    if not path(node,p1,n1) or not path(node,p2,n2):
        return -1
    i = 0
    while i < len(p1) and i < len(p2):
        if p1[i] != p2[i]:
            break
        i += 1
    return p1[i-1]

#zig zag traversal

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
    arr = []
    #ans = pairsum(root,3)
    #ans = inorder(root,arr)
    ans = lca(root,1,3)
    print(ans)


