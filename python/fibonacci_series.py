def fibonacci(n):
    if n < 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(10):
    print(fibonacci(i),end="")
    
    
a=0
b=1
n=10
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
print(a,end=" ")