# write a program that prints square of each number of a list
l= [1, 2, 3]

# with for loop
for i in range(0, len(l)):
    print(l[i] * l[i])

print("-----------------")
# with while loop
i = 0
while i < len(l):
    print(l[i] * l[i])
    i = i + 1