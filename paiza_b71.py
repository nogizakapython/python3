import sys
sys.setrecursionlimit(10**6)
def recursive(x,d,n):
    if n == 1:
        return x
    elif n > 1:
        return recursive(x,d,n-1) + d

x,d = map(int,input().split(' '))
count = int(input())
for i in range(count):
    n = int(input())
    ans = recursive(x,d,n)
    print(ans)
