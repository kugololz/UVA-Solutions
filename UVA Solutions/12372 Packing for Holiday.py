t = int(input())
c = 1
for x in range(0,t):
    l,w,h = map(int, input().split())

    if l <= 20 and w<=20 and h<=20:
        print(f"""Case {c}: good""")
    else:
        print(f"""Case {c}: bad""")

    c+=1
