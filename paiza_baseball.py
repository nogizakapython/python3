def hantei(s_count,b_count,msg):
    if s_count == 3:
        print("out!")
    elif b_count == 4:
        print("fourball!")
    else:
        print(msg + "!") 

def main():
    num = int(input())
    s_count = 0
    b_count = 0
    for i in range(num):
        data = input()
        if data == "strike":
            s_count += 1 
        else:
            b_count += 1
        hantei(s_count,b_count,data)

if __name__ == "__main__":
    main()
