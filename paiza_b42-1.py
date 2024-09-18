array = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]
count = {}

for pattern in array:
    if pattern in count:
        count[pattern] += 1
    else:
        count[pattern] = 1

for (key, value) in count.items():
    if value != 1:
        print(value)
