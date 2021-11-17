n= input().split()
a= int(n[0])
b= int(n[1])
if a>b:
    print("O JOGO DUROU "+str((24-a+b))+" HORA(S)")
elif a==b:
    print("O JOGO DUROU 24 HORA(S)")
elif a<b:
    print("O JOGO DUROU "+str(b-a)+" HORA(S)")
