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
    #arr = []
    if node == None:
        return None
    else:
        inorder(node.left,arr)
        arr.append(node.data)
        inorder(node.right,arr)
    return arr
    
def pairsum(node,sumi):
    arr1 = []
    arr2 = inorder(node,arr1)
    end = len(arr2)-1
    start = 0
    while start < end:
        if sumi == arr2[start] + arr2[end]:
            print(arr2[start], arr2[end])
            return True    
        if sumi < arr2[start] + arr2[end]:
            end -= 1
        if sumi > arr2[start] + arr2[end]:
            start += 1
    return False

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
    ans = pairsum(root,3)
    print(ans)