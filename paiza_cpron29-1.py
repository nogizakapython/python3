N = int(input())

binaryNumber = list()
while N // 2 > 0:
    binaryNumber.append(N % 2)
    N //= 2
binaryNumber.append(N)
reversed(binaryNumber)  # 逆順にする

ans = 0
for i in range(len(binaryNumber)):
    if binaryNumber[i] == 1:
        ans += 1
print(ans)
