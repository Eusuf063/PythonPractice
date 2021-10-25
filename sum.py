def sum(n):
    x = 0
    for i in range(1, n+1):
        x = x + i
    return x

def factorial(n):
    x = 1
    for i in range(1, n + 1):
        x = x * i
    return x;

while True:
    p = int(input())
    print(sum(p))
    n = int(input())
    r = int(input())

    nPr = factorial(n) / ((factorial(r) * factorial(n-r)))

    # i = 1
    # fac_n = 1
    # for i in range(1, n+1):
    #     fact_n = fact_n * i
    #
    # i = 1
    # fact_r = 1
    # for i in range(1, r + 1):
    #     fact_r = fact_r * i
    #
    #




