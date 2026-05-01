def longest_subb_string(s):
    s = "abcabcbb"
    seen=[]
    left=0
    max_length=0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.append(s[right])
        max_length=max(max_length,right - left +1)
    return max_length        
print(longest_subb_string("abcabcbb"))