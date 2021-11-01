a = int(input())
print(str(int(a / 365)) + " ano(s)")
a = a % 365
print(str(int(a / 30)) + " mes(es)")
a = a % 30
print(str (a) + " dia(s)")