n= input().split()
a= float(n[0])
b= float(n[1])
c= float(n[2])
Perimetro = a+b+c
Area= ((a+b)*c)/2
if a<b+c and b<a+c and c<b+a:
    print("Perimetro = %0.1f"%Perimetro)
else:
    print("Area = %0.1f"%Area)