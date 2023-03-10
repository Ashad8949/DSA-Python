
def minWindowS(s,t):
    if t == "": return ""

    window, counter = {}, {}
    for e in t:
        counter[e] = 1 + counter.get(e, 0)
    
    have, need = 0, len(counter)
    res, res_len = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in counter and window[c] == counter[c]:
            have += 1
        
        while have == need:
            #update result 
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = (r - l + 1)
            #pop from left
            window[s[l]] -= 1
            if s[l] in counter and window[s[l]] < counter[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r+1] if res_len != float("infinity") else ""

s = "ADOBECODEBANC"
t = "ABC"

print(minWindowS(s,t))