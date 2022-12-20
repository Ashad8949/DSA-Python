
def maxSubstring(s):
    l = 0
    maxi = 0
    sub_string = set()
    for i, e in enumerate(s):
        while e in sub_string:
            sub_string.remove(s[l])
            l += 1
        sub_string.add(e)
        maxi = max(maxi, i-l+1)
    return maxi

m = maxSubstring("aaabc")
print(m)