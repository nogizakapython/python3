# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n, a, b = map(int, input().split())

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    if i >= a:
        dp[i] += dp[i - a]
    if i >= b:
        dp[i] += dp[i - b]

print(dp[n])
