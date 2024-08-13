num1 = int(input())
for i in range(num1):

    nickname,old,birth,state = map(str,input().split(" "))
    
    print("User{")
    print("nickname : " + nickname)
    print("old : "+ old)
    print("birth : " + birth)
    print("state : " + state)
    print("}")