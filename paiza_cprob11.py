hit_number = int(input())
s_hitnumber = hit_number % 10000
t_hitnumber = hit_number % 1000
num = int(input())
for i in range(num):
    n = int(input())
    sn = n % 10000
    tn = n % 1000
    if n == hit_number:
        print("first")
    elif n-1 == hit_number or n+1 == hit_number:
        print("adjacent")
    elif sn == s_hitnumber:
        print("second")
    elif tn == t_hitnumber:
        print("third")
    else:
        print("blank")
