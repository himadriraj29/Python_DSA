def zerosum(A):
    dis = {}
    sumi = 0
    for i in A:
        sumi += i
        if sumi == 0:
            return True
        if sumi in dis:
            return True 
        dis[sumi] = 0 
    return False


if __name__ == "__main__":
    ans = zerosum([2,-3,-1,2,3,-4,5,4])
    print(ans)