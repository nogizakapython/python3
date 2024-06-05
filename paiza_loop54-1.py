a, b = [int(x) for x in input().split()]

if a <= 0 and b >= 0:
    # a から b の間に 0 が含まれる
    print(a * b)
elif a > 0:
    # a と b が両方とも正の数
    print(a * a)
else:
    # a と b が両方とも負の数
    print(b * b)
