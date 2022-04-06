def max_diff(arr):
    res_maxi = arr[1] - arr[0]
    mini_element = arr[0]
    n = len(arr)
    for i in range(1,n):
        res_maxi = max(res_maxi,arr[i]-mini_element)
        mini_element = min(mini_element,arr[i])
    return res_maxi

arr = [45,76,90,12,43]
ans = max_diff(arr)
print(ans)

