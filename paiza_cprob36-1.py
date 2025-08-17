def solve():
    tag_a, tag_b = input().split()
    search_str = input()
    m = len(tag_a)
    a_index,b_index = map(int,input().split())
    if a_index+m == b_index:
        print('<blank>')
    else:
        print(search_str[a_index+m-1:b_index-1])
if __name__ == "__main__":
    solve()
