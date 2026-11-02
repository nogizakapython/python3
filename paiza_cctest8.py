# a が b 以下かつ a + b が c 以下であるなら "Yes" を、そうでないなら "No" を出力してください。
a, b, c = list(map(int, input().split()))
if a <= b and a + b <= c:
    print('Yes')
else:
    print('No')