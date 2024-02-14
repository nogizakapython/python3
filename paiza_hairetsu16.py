array1 = [[1,3,5,7],[8,1,3,8]]
ans = ""
num1 = len(array1)
for i in range(num1):
    num2 = len(array1[i])
    for j in range(num2):
        if j == num2 - 1:
            ans = ans + str(array1[i][j])
        else:
            ans = ans + str(array1[i][j]) + " "

    print(ans)
    ans = ""
