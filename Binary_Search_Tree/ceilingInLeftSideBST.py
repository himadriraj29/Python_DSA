import bisect
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

#naive approach
def ceilOnLeft(arr):
    A = []
    n = len(arr)
    A.append(-1)
    for i in range(n):
        diff = float('inf')
        for j in range(i):
            if arr[j] >= arr[i]:
                diff = min(diff,arr[j] - arr[i])
        if(diff == float('inf')):
            A.append(-1)
        else:
            A.append(arr[i] + diff)
    return A

#optimized approach using treeset: bisect in python
def ceil_bisect(arr): 
    n = len(arr)
    ans = []
    if n == 1:
        ans.append(-1) 
        return
    sortedArr = list(arr)
    sortedArr.sort()  
    for i in range(n):
        it = bisect.bisect_right(sortedArr,arr[i])
        if (it-1) != 0 and sortedArr[it-2] == arr[i]:
            ans.append(arr[i])
        elif it <= n-1:
            ans.append(sortedArr[it])
        else:
            ans.append(-1)
    return ans

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
    arr = [10,5,11,10,20,12]
    #ans = ceilOnLeft(arr)
    ans = ceil_bisect(arr)
    print(ans)

