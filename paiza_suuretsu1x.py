N = int(input())

A = list(map(int,input().split()))

ans_arith = "Yes"

#隣接 2 項間の差分を求め、すべて等しければ Yes、そうでなければ No → 1 ≦ i ≦ N - 2 を満たす i で A_{i + 2} - A{i + 1} = A_{i + 1} - A_i が成り立てば Yes、そうでなければ No 
for i in range(N - 2):
    if A[i + 2] - A[i + 1] != A[i + 1] - A[i]:
        ans_arith = "No"

print(ans_arith)

ans_geo = "Yes"

#等比数列と同じように求める。誤差に注意し、A_{i + 2} × A_i = A_{i + 1} × A_{i + 1} で判定
for i in range(N - 2):
    if A[i + 2] * A[i] != A[i + 1] ** 2:
        ans_geo = "No"

print(ans_geo)