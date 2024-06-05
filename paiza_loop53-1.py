h, w = [int(x) for x in input().split()]

if h == 0 or w == 0:
    print("NO")
elif h % 2 == 0 and w % 2 == 0:
    print("YES")
else:
    print("NO")
