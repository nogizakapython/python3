def solve():
    tag_a, tag_b = input().split()
    search_str = input()
    n,m = len(search_str),len(tag_a)
    a_index = search_str.find(tag_a)+1
    b_index = search_str.find(tag_b)+1
    print(a_index,b_index)
if __name__ == "__main__":
    solve()
