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
    ans = recoverTree(root)
    print(ans)


