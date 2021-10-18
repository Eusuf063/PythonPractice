def copy_first_list_to_second_list(list1, list2):
    for x in list1:
        list2.append(x)

l1 = [1, 2, 3]
l2 = []

copy_first_list_to_second_list(l1, l2)
print(l1)
print(l2)

print("------------------------------------")

