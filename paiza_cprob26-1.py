N = int(input())
ans = 0
bitMask = 1
while bitMask <= N:
    if bitMask & N != 0:
        ans += 1
    bitMask *= 2

print(ans)
