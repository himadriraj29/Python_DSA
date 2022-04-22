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


def preorder(node):
    if node == None:
        return 
    st = []
    ans = []
    st.append(node)
    while len(st) > 0:
        #st.append(node)
        node = st.pop()
        ans.append(node.data)

        if node.right != None:
            st.append(node.right)
        if node.left != None:
            st.append(node.left)
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
    ans = preorder(root)
    print(ans)

