# Let's チャレンジ！！
import sys
sys.setrecursionlimit(10**6)

def recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n >= 3:
        return recursive(n-1) + recursive(n-2)

n = int(input())
ans = recursive(n)
print(ans)
