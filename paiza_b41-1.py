array = ["HND", "NRT", "KIX", "NGO", "NGO"]
duplicate = False

for i in range(len(array)):
    for j in range(len(array)):
        if i != j and array[i] == array[j]:
            duplicate = True

if duplicate:
    print("true")
else:
    print("false")
