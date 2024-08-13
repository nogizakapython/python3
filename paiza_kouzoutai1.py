num1 = int(input())
for i in range(num1):
    data1 = input()
    array1 = data1.split(" ")
    nickname = array1[0]
    old = array1[1]
    birth = array1[2]
    state = array1[3]
    
    print("User{")
    print("nickname : " + nickname)
    print("old : "+ old)
    print("birth : " + birth)
    print("state : " + state)
    print("}")