def intersection(A,B):
    dis = {}
    for i in A:
        if i not in dis:
            dis[i] = 0
    for i in B:
        if i in dis:
            dis[i] += 1
    for i in dis:
        if dis[i] >= 1:
            print(i)


if __name__ == "__main__":
    ans = intersection([2,3,1,2,3,4,5,4],[1,3,4,5,6,7])
    print(ans)