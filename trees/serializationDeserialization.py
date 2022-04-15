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


def serialization(node):
    empty = -1
    arr = []
    if node == -1:
        arr.append(empty)
        return 
    arr.append(node.data)
    serialization(node.left)
    serialization(node.right)
    return arr

def deserialize(arr):
    idx = 0
    if idx == len(arr):
        retun None
    val = arr.get(idx)
    idx += 1
    if val == empty:
        return None
    node= Node(val)
    node.left = deserialize(arr)
    node.right = deserialize(arr)
    return node


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
    ans = serialization(root)
    print(ans)

