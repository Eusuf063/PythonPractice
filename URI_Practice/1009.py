def bonus_function(a,b):
    Total = a+b*0.15
    return Total
name= input()
salary =float(input())
product=float(input())
#print(bonus_function(salary,product))
print("TOTAL = R$ %.2f"%bonus_function(salary,product))

