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


def verticalTraverse(node,hd,disc):
    if node == None:
        return
    verticalTraverse(node.left,hd-1,disc)

    if(hd in disc.keys()):
        disc[hd] = disc[hd] + node.data
    else:
        disc[hd] = node.data
    
    verticalTraverse(node.right,hd+1,disc)

def verticalSum(node):
    disc = {}
    verticalTraverse(node,0,disc)
    for i,j in disc.items():
        print(i, ' = ',j, end = '  ')


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
    #arr = []
    #ans = pairsum(root,3)
    ans = verticalSum(root)
    #print(ans)