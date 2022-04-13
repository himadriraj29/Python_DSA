def Union(A,B):
    dis = {}
    for i in A:
        if i not in dis:
            dis[i] = 0
    for i in B:
        if i not in dis:
            dis[i] = 0
    return dis


if __name__ == "__main__":
    ans = Union([2,3,1,2,3,4,5,4],[1,3,4,5,6,7])
    print(ans)