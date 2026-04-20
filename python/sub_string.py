s= "ramanareddy"
n=len(s)
sub_str=[]
for i in range(n):
    for j in range(i+1,n+1):
        sub_str.append(s[i:j])
print(sub_str)