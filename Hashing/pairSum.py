def pairsum(A,s):
    dis = {}
    for i in A:
        if s - i in dis:
            return True
        elif i not in dis:
            dis[i] = 0
    return False

if __name__ == "__main__":
    ans = pairsum([2,3,4,12,10],17)
    print(ans)
