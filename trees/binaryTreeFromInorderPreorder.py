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

def search(arr,s,e,val):
    for i in range(s,e+1):
        if arr[i] == val:
            return i
    
def btInorderPre(I,Pr,s,e):
    if s > e:
        return
    tnode = Node(Pr[btInorderPre.Prindx])
    btInorderPre.Prindx += 1

    if s == e:
        return tnode

    indx = search(I,s,e,tnode.data)
    tnode.left = btInorderPre(I,Pr,s,indx-1)
    tnode.right = btInorderPre(I,Pr,indx+1,e)
    return tnode

if __name__ == "__main__":
    #root = buildTree()
    #print(node)
    '''
    node = Node(1)
    node.left = Node(2)
    node.left.left = Node(8)
    node.left.right = Node(7)
    node.right = Node(3)
    '''
    #arr = []
    #ans = pairsum(root,3)
    #ans = inorder(root,arr)
    I = ['D', 'B', 'E', 'A', 'F', 'C']
    Pr = ['A', 'B', 'D', 'E', 'C', 'F']
    btInorderPre.Prindx = 0
    ans = btInorderPre(I,Pr,0,5)
    print(ans.data)
    print(ans.left.data)
    print(ans.right.data)
