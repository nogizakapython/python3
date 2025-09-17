class Member:
    def __init__(self,name,old,birth,state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state


n = int(input())
rouster = [None] * n

for i in range(n):
    name, old, birth, state = input().split()
    rouster[i] = Member(name, old, birth, state)

place = input()
for member in rouster:
    if member.state == place:
        print(member.name)
