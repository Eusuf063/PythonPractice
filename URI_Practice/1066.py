count=0
even=0
odd=0
pos=0
neg=0
for i in range(5):
    n = int(input())
    if(n%2==0):
        even=even+1
    else:
        odd=odd+1
    if (n>0):
        pos=pos+1
    elif (n<0):
        neg=neg+1
print(even,"valor(es) par(es)")
print(odd, "valor(es) impar(es)")
print(pos, "valor(es) positivo(s)")
print(neg,"valor(es) negativo(s)")