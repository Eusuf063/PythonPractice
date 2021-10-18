# write a program that will take element from one list and will insert to another list
list1 = [1, 2, 3]
list2 = []

print("list1: ")
print(list1)

print("list2: ")
print(list2)

print("-----------------")
for x in list1:
    list2.append(x)

print("list1: ")
print(list1)

print("list2: ")
print(list2)


print("------------------------")
list3 = ["a", "1", "21a", "asd"]
list4 = [m for m in list3 if "a" in m]
# list4 = list3
list3[0] = "b"

print(list3)

print(list4)
a = 2
b = a
a = 3
print(a)
print(b)

