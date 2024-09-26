n = 5
m_count = 0
b_count = 0
for i in range(n):
    data = input()
    if data == "OOOOO":
        m_count += 1
    if data == "XXXXX":
        b_count += 1
if m_count >= 1:
    print("O")
elif b_count >= 1:
    print("X")
else:
    print("D")
