
def maxProfit(arr):
    l = 0
    maxi = 0
    for r,cp in enumerate(arr):
        if arr[l] > cp:
            l = r
        else:
            profit = cp - arr[l]
            maxi = max(maxi, profit)

    return maxi

arr = list(map(int, input().split()))
print(maxProfit(arr))