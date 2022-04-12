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
    return max(lh,rh) + 1
'''
#naive approach: complexity o(n2)
def balancedBT(node):
    if node == None:
        return True
    else:
        l = height(node.left)
        r = height(node.right)

        if abs(l-r) < 1 and balancedBT(node.left) and balancedBT(node.right):
            return True
    return False
'''
#optimized approach: complexity o(n)
def isBalancedBT(node):
    if node == None:
        return 0
    l = isBalancedBT(node.left)
    if l == -1:
        return -1
    r = isBalancedBT(node.right)
    if r == -1:
        return -1
    if abs(l-r) > 1:
        return -1
    else: 
        return max(l,r) + 1   # returns height




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
    ans = isBalancedBT(root)
    print(ans)
