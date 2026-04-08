class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self):
        return self.number

    def getname(self):
        return self.name


n = int(input())

roster = []
for _ in range(n):
    values = input().split()

    query = values[0]
    if query == "make":
        number = int(values[1])
        name = values[2]
        roster.append(Employee(number, name))
    elif query == "getnum":
        index = int(values[1]) - 1
        number = roster[index].getnum()
        print(number)
    else:
        index = int(values[1]) - 1
        name = roster[index].getname()
        print(name)