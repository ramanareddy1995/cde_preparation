def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item,list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
lst = [1, 2, [3, 4], [5,[6, 7]], 8]
print(flatten(lst))        
    