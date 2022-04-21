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

prev = Node(-1)
def fixBST(node):
    global prev
    first = None
    Second = None
    if node == None:
        return
    fixBST(node.left)
    if prev != None and node.data < prev.data:
        if first == None:
            first = prev
        Second = node
    prev = node
    fixBST(node.right)
    first,Second = Second,first
    return [first,Second]

#my method
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
    ans = fixBST(root)
    print(ans[0].data)
    print(ans[1].data)
    print(root.data,root.left.data,root.right.data)