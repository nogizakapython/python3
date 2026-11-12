N = int(input())
S = []
for i in range(N):
    S.append(input())
P = input()

for si in S:
    if len(si) < len(P):  # |S_i| < |P|の場合, PはS_iのプレフィックスにはならない
        print("/")
        continue

    si += "#"
    is_prefix = True
    for i in range(len(P)):  # プレフィックスではない
        if si[i] != P[i]:
            print("/")
            is_prefix = False
            break

    if is_prefix:
        print(si[len(P)])  # プレフィックスである。S_iの|P|+1文字目を出力