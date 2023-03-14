file_name = "file_test4.txt"

names = ["Jiro","Saburo","Siro"]

with open(file_name, mode="a") as f:
    for name in names:
        f.write(f"{name}\n")
