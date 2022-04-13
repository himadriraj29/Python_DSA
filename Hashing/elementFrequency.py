def frequency(A):
    dis = {}
    for i in A:
        if i not in dis:
            dis[i] = 0
    for i in A:
        if i in dis:
            dis[i] += 1    
    return dis


if __name__ == "__main__":
    ans = frequency([2,3,1,2,3,4,5,4])
    print(ans)