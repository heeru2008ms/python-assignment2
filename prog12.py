basic = int(input("Enter Basic salary: "))
if basic <= 10000:
    hra = basic * 20/100
    da = basic * 80/100
elif basic <= 20000:
    hra = basic * 25/100
    da = basic * 90/100
elif basic > 20000:
    hra = basic * 30/100
    da = basic * 95/100
Gross = basic + hra + da
print("HRA = ", hra)
print("DA  = ", da)
print("Gross Salary = ", Gross)
