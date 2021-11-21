count = 0
sum = 0
for i in range(1, 7):
    n = float(input())
    if (n > 0):
        count = count + 1
        sum = sum + n
print(count, "valores positivos")
print("%0.1f" % (sum / count))
