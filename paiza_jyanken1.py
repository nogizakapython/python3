N = int(input())
A_win_count = 0
for i in range(N):
    data = input()
    array1 = data.split(' ')
    A = array1[0]
    B = array1[1]
    if A == "G" and B == "C":
        A_win_count += 1
    if A == "C" and B == "P":
        A_win_count += 1
    if A == "P" and B == "G":
        A_win_count += 1
print(A_win_count)
