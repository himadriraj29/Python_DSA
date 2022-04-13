def longestKsum(A,k):
    dis = {}
    sumi = 0
    max_idx = 0
    res = float("-inf")
    n = len(A)
    for i in range(n):
        sumi += A[i]
        if sumi == k:
            #idx = abs(i - dis[sumi])
            #max_idx = max(max_idx,idx)
            #return True
            dis[sumi] = i
            if i+1>res:
                res = i+1
        elif sumi - k in dis:
            #idx = abs(i - dis[sumi-k])
            #max_idx = max(max_idx,idx)
            #return True
            temp = i-dis[sumi-k]
            if temp>res:
                res = temp
        if sumi not in dis:
            dis[sumi]=i
    print(dis)
    return res


if __name__ == "__main__":
    ans = longestKsum([1,-1,1,-1,-1,-1,1,1,1,-1,-1,1],0)
    print(ans)