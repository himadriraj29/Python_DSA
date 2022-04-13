def ksum(A,k):
    dis = {}
    sumi = 0
    for i in A:
        sumi += i
        if sumi == k:
            return True
        if i - k in dis:
            return True
        else: 
            dis[sumi] = 0   
    return False


if __name__ == "__main__":
    ans = ksum([2,3,1,2,3,4,5,4],110)
    print(ans)