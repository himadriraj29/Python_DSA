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

def path(node,p,n):
    if node == None:
        return False
    p.append(root)
    if node.data == n:
        return True
    if path(node.left,p,n) or path(node.right,p,n):
        return True
    p.pop()    
    return False

def lca(node,n1,n2):
    p1 = []
    p2 = []
    if path(node,p1,n1) == False or path(node,p2,n2) == False:
        return None
    i = 0
    while i < len(p1) and i < len(p2):
        if p1[i] != p2[i]:
            break
        i += 1
    return p1[i-1].data
    
def lcaa(node,n1,n2):
    if node == None:
        return None
    if node.data == n1 or node.data == n2:
        return node

    l = lcaa(node.left,n1,n2)
    r = lcaa(node.right,n1,n2)

    if l and r:
        return node
    if l != None:
        return l
    else:
        return r       
        
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
    p = []
    ans = lcaa(root,2,3)
    print(ans.data)
    

    #tree inorder used here [2 1 3]
