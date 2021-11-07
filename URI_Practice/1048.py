n=float(input())
if 0<n and n<=400.00:
    print("Novo salario: %0.2f"%(n*(1+.15)))
    print("Reajuste ganho: %0.2f"%(n*.15))
    print("Em percentual: "+str(round(n*.15*100/n))+" %")
elif 400.00<n and n<=800.00:
    print("Novo salario: %0.2f"%(n*(1+.12)))
    print("Reajuste ganho: %0.2f"%(n*.12))
    print("Em percentual: "+str(round(n*.12*100/n))+" %")
elif 800.00<n and n<=1200.00:
    print("Novo salario: %0.2f"%(n*(1+.10)))
    print("Reajuste ganho: %0.2f"%(n*.10))
    print("Em percentual: "+str(round(n*.10*100/n))+" %")
elif 1200.00<n and n<=2000.00:
    print("Novo salario: %0.2f"%(n*(1+.07)))
    print("Reajuste ganho: %0.2f"%(n*.07))
    print("Em percentual: "+str(round(n*.07*100/n))+" %")
elif n>2000.00:
    print("Novo salario: %0.2f"%(n*(1+.04)))
    print("Reajuste ganho: %0.2f"%(n*.04))
    print("Em percentual: "+str(round(n*.04*100/n))+" %")