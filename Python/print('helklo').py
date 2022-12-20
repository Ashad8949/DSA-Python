def Search(arr,target):
    r = 0
    c = len(arr)-1
    while r<len(arr) and c>=0:
        if arr[r][c]==target:
            return [r,c]
        elif arr[r][c]>target:
            c-=1
        else:
            r+=1
    return [-1,-1]

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(Search(arr,4))