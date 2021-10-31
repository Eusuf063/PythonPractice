m = input().split(" ")
a= int((m[0]))
b= int((m[1]))
c= int((m[2]))
maior = ((a) + (b) + abs((a) - (b))) / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c))) / 2
print("%d eh o maior" %resultado)
