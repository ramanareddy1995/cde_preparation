num=[1,2,3,4,5,6,4,6,7,3,6,8,9]
uniq=[]
dup=[]
for i in num:
    if i in uniq and i not in dup:
        dup.append(i)
    else:
        uniq.append(i)
dup.sort()
print(dup)
 

                 