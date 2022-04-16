'''
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

def ceilbst(node,key):
    res = Node(None)
    while node != None:
        if node.data == key:
            return node           
        elif node.data < key:
            node = node.right
        else:
            res = node
            node = node.left
    return res

    

if __name__ == "__main__":
    root = buildTree()
    #print(root)

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(8)
    root.left.right = Node(7)
    root.right = Node(3)

    ans = ceilbst(root,4)
    print(ans.data)

'''

a = "abcde"
print(a[-2:])