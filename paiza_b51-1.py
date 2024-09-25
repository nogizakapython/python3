str1 = input()
m_count = 0
b_count = 0
leng1 = len(str1)
for i in range(leng1):
    c = str1[i]
    if c == "O":
        m_count += 1
    if c == "X":
        b_count += 1
if m_count == 5:
    print("O")
elif b_count == 5:
    print("X")
else:
    print("D")
