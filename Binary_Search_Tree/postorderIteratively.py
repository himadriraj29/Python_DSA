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

#using 2 stacks 
#step 1: make 2 stacks, s1 and s2:
#step 2: push root into s1 
#step 3: now pop it and push it into s2
#step 4: check for its(popped one) left and right child respectively and push it intro s1
#step 5: now repeat the process : keep popping form s1 and adding it to s2 while checking if left or right node is present or not:
#step 6: if yes keep adding it on s1
def postorder(node):
    if node == None:
        return 
    st1 = []
    st2 = []
    ans = []
    st1.append(node)
    while st1:
        #st.append(node)
        node = st1.pop()
        st2.append(node)

        if node.left != None:
            st1.append(node.left)
        if node.right != None:
            st1.append(node.right)

    while st2:
        node = st2.pop()
        ans.append(node.data)
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
    ans = postorder(root)
    print(ans)

