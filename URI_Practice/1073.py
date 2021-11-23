N=int(input())
if 5<N<2000:
    for i in range(1,N+1):
        if i%2==0:
            print(str(i)+"^"+str(2)+" =",(i**2))