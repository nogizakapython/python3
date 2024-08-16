word_list = input().split()
order = []
count = []
for word in word_list:
    if word in order:
        count[order.index(word)] += 1
    else:
        count.append(1)
        order.append(word)
        print(word)
for c in count:
    print(c)
