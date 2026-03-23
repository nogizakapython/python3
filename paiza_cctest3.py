from functools import cmp_to_key

# カスタム比較関数
def compare(a, b):
    # 文字列として結合したときに、どちらが大きくなるかを比較
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0

numbers = input().split()

numbers.sort(key=cmp_to_key(compare))

print("".join(numbers))