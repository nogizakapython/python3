n, q = map(int, input().split())
students = list(range(1, n + 1))

for _ in range(q):
    s = input().split()
    if s[0] == "swap":
        a = int(s[1]) - 1
        b = int(s[2]) - 1
        tmp = students[a]
        students[a] = students[b]
        students[b] = tmp
    elif s[0] == "reverse":
        students.reverse()
    else:
        c = int(s[1])
        if len(students) > c:
            students = students[:c]

for student in students:
    print(student)
