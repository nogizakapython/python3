word_list = input().split()
order = []

for word in word_list:
    if word in order:
        print("already_been")
    else:
        order.append(word)
        print(word)