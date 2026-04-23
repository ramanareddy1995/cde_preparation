from collections import Counter
num=[1,1,1,2,2,3,3,3,3,4,5]
k=2
freq=Counter(num)
result=sorted(freq,key=freq.get,reverse=True)[:k]
print(result)



num=[1,1,1,2,2,3,3,3,3,4,5]
k=2
freq={}
for i in num:
    freq[i]=freq.get(i,0)+1
result=sorted(freq,key = freq.get,reverse = True)[:k]
print(result)    