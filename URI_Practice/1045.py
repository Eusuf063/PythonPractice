n = input().split()
n.sort()
n.reverse()
A = float(n[0])
B = float(n[1])
C = float(n[2])
if A >= (B + C):
    print("NAO FORMA TRIANGULO")
elif (A * A) == (B * B) + (C * C):
    print("TRIANGULO RETANGULO")
elif (A * A) > (B * B) + (C * C):
    print("TRIANGULO OBTUSANGULO")
elif (A * A) < (B * B) + (C * C):
    print("TRIANGULO ACUTANGULO")
elif A == B and B == C:
    print("TRIANGULO EQUILATERO")
elif A == B or B == C:
    print("TRIANGULO ISOSCELES")

#if(a>=(b+c)):
#    print("NAO FORMA TRIANGULO")
#elif(a*a == (b*b+c*c)):
#     print("TRIANGULO RETANGULO")
#elif(a * a > (b*b+ c*c)):
#    print("TRIANGULO OBTUSANGULO")
#elif(a*a<(b*b + c*c)):
#    print("TRIANGULO ACUTANGULO")
#if(a == b and b == c):
#        print("TRIANGULO EQUILATERO")
#elif(a == b or b == c):
#        print("TRIANGULO ISOSCELES")