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
preidx = 0
def treeConst(ino,pre,s,e):
    global preidx
    if s > e:
        return None
    root = Node(pre[preidx])
    preidx+=1
    for i in range(s,e+1):
        if ino[i] == root.data:
            idx = i
            break
    root.left = treeConst(ino,pre,s,idx-1)
    root.right = treeConst(ino,pre,idx+1,e)
    return root


if __name__ == "__main__":
    #root = buildTree()
    #print(root)
    '''
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(8)
    root.left.right = Node(7)
    root.right = Node(3)
    '''
    ino = [2,1,3]
    pre = [1,2,3]
    ans = treeConst(ino,pre,0,2)
    print(ans.data)
    print(ans.left.data)
    print(ans.right.data)

    