s1 = "name,age,city"
s2 = "ram,25,hyderabad"
keys = s1.split(",")
values = s2.split(",")
z=dict(zip(keys,values))
print(z)