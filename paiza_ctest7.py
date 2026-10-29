# a + b が c 以下であるなら "Yes" を、そうでないなら "No" を出力してください。
a, b, c = map(int,input().split())
if a + b <= c:
    print('Yes')
else:
    print('No')
