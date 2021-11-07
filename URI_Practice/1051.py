salary = float(input())
if 0 <= salary <= 2000.00:
    print("Isento")
elif 2000.01 <= salary <= 3000.00:
    tax = (salary-2000)* .08
    print("R$ %.2f" % tax)
elif 3000.01 <= salary <= 4500.00:
    tax = (salary - 3000.00) * 0.18 + 80.00
    print("R$ %.2f" % tax)
elif salary > 4500:
    tax = (salary - 4500) * 0.28 + 350.00
    print("R$ %.2f" % tax)
