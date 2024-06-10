# Use LC 3
def length(s):
    left, right = 0, 0
    ans = 0
    window = dict()

    while right < len(s):
        if s[right] not in window:
            window[s[right]] = 1
        else:
            window[s[right]] += 1

        while window[s[right]] > 1:
            window[s[left]] -= 1
            left += 1

        ans = max(ans, right - left + 1)
        right += 1
    
    return ans
     