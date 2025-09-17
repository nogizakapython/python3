# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
def output1(nickname,old,birthday,state):
    print("User{")
    print(f'nickname : {nickname}')
    print(f'old : {old}')
    print(f'birth : {birthday}')
    print(f'state : {state}')
    print('}')

def main():
    n = int(input())
    for i in range(n):
        a,b,c,d = input().split(' ')
        output1(a,b,c,d)

if __name__ == "__main__":
    main()
