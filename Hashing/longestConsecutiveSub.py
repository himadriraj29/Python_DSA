def getSub(A):
    sub = {}
    for i in A:
        if i not in sub:
            if i - 1 in sub and i+1 in sub:
                sub[i] = sub[i-1] + sub[i+1] + 1
                sub[i-1] = sub[i]
                sub[i+1] = sub[i]
            elif i+1 in sub:
                sub[i] = sub[i+1] + 1
                sub[i+1] = sub[i]
            elif i-1 in sub:
                sub[i] = sub[i-1] + 1
                sub[i-1] = sub[i]
            else:
                sub[i] = 1
    return sub

if __name__ == "__main__":
    ans = getSub([1,9,3,4,2,20])
    print(ans)