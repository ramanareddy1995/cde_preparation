from collections import Counter
nums=[1,2,2,2,3,3,3,3,4,4,4,5]
freq=Counter(nums)
sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
print(sorted_freq[1][0])