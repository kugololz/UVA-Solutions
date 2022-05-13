from math import sqrt

test = int(input())

for i in range(test):
    n = int(input())
    raiz = int(sqrt(2 * n))

    if (raiz*(raiz+1))//2 > n:
        raiz -= 1

    print(raiz)