infile = "NCM29_202310.log"
with open(infile,mode="r") as f:
    for line in f:
        line1 = line.replace("\n","")
        print(line1)