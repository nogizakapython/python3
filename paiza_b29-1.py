pattern = input()
string = input()
result = 0

for i in range(len(string) - len(pattern) + 1):
    portion = string[i : i + len(pattern)]

    if portion == pattern:
        result += 1

print(result)
