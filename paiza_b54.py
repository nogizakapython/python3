array1 = []

for i in range(5):
    data = input()
    array1.append(data)

m_flag = 0
b_flag = 0

for j in range(5):
    m_count = 0
    b_count = 0
    for word in array1:
        c = word[j]
        if c == "O":
            m_count += 1
        elif c == "X":
            b_count += 1
    if m_count == 5:
        m_flag = 1
        break
    elif b_count == 5:
        b_flag = 1
        break
if m_flag == 1:
    print("O")
elif b_flag == 1:
    print("X")
else:
    print("D")
