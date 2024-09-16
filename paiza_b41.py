array1 = ["HND", "NRT", "KIX", "NGO", "NGO"]
array2 = list(set(array1))
count = 0
for i in array2:
    if i in array1:
        count += 1
if count > 0:
    print("true")
else:
    print("false")
