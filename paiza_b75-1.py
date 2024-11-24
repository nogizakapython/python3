class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state

    def change_name(self, name):
        self.name = name


n, k = [int(x) for x in input().split()]

roster = [None] * n
for i in range(n):
    name, old, birth, state = input().split()
    roster[i] = Student(name, old, birth, state)

for i in range(k):
    index, new_name = input().split()
    roster[int(index) - 1].change_name(new_name)

for student in roster:
    print(student.name, student.old, student.birth, student.state)
