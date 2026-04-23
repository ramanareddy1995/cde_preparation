num = [2,3,4,5,6,7,8]
target = 10
pairs = []
for i  in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] + num[j] == target:
            pairs.append((num[i], num[j]))
print(pairs)