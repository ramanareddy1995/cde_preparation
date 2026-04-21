s="i love my country"
words=s.split()
result=[]
for word in words:
    result.append(word[::-1])
print(" ".join(result))