s = "ramanareddy"
freq={}
for i in s:
    freq[i] = freq.get(i,0)+1
for k, v in freq.items():
    print(k ,":",v)
for i in s:
    if freq[i] == 1:
        print(i)