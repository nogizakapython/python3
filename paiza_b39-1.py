num = int(input())
inputs = {}

for i in range(num):
    tmp = input().split()
    inputs[int(tmp[1])] = tmp[0]

inputs = sorted(inputs.items())

for i in inputs:
    print(i[1])
