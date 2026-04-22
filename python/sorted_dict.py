emp_salary = {
    "Ram": 50000,
    "Ravi": 70000,
    "Sita": 60000,
    "John": 55000
}
# sorted by keys 
d1 = sorted(emp_salary.items(), key = lambda x:x[0])
print(d1)
# sorted by values
d2 = sorted(emp_salary.items(), key = lambda x:x[1])
print(d2)
