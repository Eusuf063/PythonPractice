# write a program that prints square of each number of a list
l = [1, 2, 3]

# with for loop
def func1():
    print('func1')

for i in range(0, len(l)):
    print(l[i] * l[i])
    func1()

print("-----------------")
# with while loop
i = 0
while i < len(l):
    print(l[i] * l[i])
    i = i + 1

print("-----------------------")
for x in l:
    print(x * x)