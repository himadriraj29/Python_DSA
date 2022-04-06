def leader(arr):
    n = len(arr)
    temp = []
    curr_lead = arr[n-1]
    temp.append(curr_lead)
    for i in range(n-2,0,-1):
        if arr[i] > curr_lead:
            curr_lead = arr[i]
            temp.append(curr_lead)
    return temp

arr = [45,76,90,12,43]
ans = leader(arr)
print(ans)
