# 3 employee, their salary and sold products are taken as input.
# Now find out the bonus 15% by name.where name will be input
# close the program while name is E

def bonus_function(a,b):
    Total = a+b*0.15
    return Total

dict = {
}
m=int(input())
for i in range(0,m):
    name=input()
    salary =float(input())
    product=float(input())
    dict[name]=bonus_function(salary,product)
while True:
    name= input()
    # if name == "E":
    #     break
    if(name in dict.keys()):
        print(dict[name])
    else:
        print("no value exist")


