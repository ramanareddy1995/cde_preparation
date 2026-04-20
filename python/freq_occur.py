s="ramanareddy"
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
print(freq)

most_occured=max(freq,key=freq.get)
print(most_occured)
most_occured_freq=max(freq.values())
print(most_occured_freq)

for k,v in freq.items():
    print(k,":",v)