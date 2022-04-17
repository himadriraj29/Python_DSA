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