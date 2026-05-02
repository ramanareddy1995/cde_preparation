def group_anagrams(strs):
    strs = ["eat","tea","tan","ate","nat","bat"]
    
    groups={}
    for word in strs:
        key=''.join(sorted(word))
        if key not in groups:
            groups[key]=[]
        groups[key].append(word)
    return list(groups.values())
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))        