word_list = input().split()
order = []
count = []
for word in word_list:
    if word in order:
        count.append(1)
    else:
        order.append(word)
        print(word)
        
for c in count:
    print(c)