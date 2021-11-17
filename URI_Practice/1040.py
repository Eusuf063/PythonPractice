n = input().split(" ")
n1= float(n[0])
n2= float(n[1])
n3= float(n[2])
n4= float(n[3])

avg= float(((n1*2)+(n2*3)+(n3*4)+(n4*1))/10)
print("Media: %.1f"%avg)
if avg>= 7.0:
    print("Aluno aprovado.")
elif 5.0<=avg<7.0:
    print("Aluno em exame.")
elif avg<5.0:
    print("Aluno reprovado.")

