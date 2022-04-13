def distinct(A):
    dis = {}
    for i in A:
        if i not in dis:
            dis[i] = 0
    return len(dis)


if __name__ == "__main__":
    ans = distinct([2,3,1,2,3,4,5,4])
    print(ans)