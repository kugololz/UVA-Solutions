t = int(input())

for x in range(0, t):
    n = int(input())
    r = (n*567)
    r = r/9
    r = r+7492
    r = r*235
    r = r/47
    r = r-498
    e = int(r)
    if e<0:
        e = e*-1
        r = [int(a) for a in str(e)]
        print(r[-2])
    else:
        r = [int(a) for a in str(e)]
        print(r[-2])