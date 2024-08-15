array1 = input().split(" ")
word = input()
length1 = len(array1)
for i in range(length1):
    data = array1[i]
    if data == word:
        print(i)
        break