a = int(input())
b = int(input())
sum=0
if a < b:
    for i in range(a, b):
       if i%2!=0:
            sum =sum+i
    print(sum)

if a>b:
    for i in range(b+1,a):
        if i%2!=0:
            sum =sum+i
    print(sum)

if a == b:
    print("0")

