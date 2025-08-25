def solve():
    tag_a, tag_b = input().split()
    search_str = input()
    n,m = len(search_str),len(tag_a)
    a_index,b_index  = [],[]
    for i in range(n-m+1):
        check_a = True
        check_b = True
        for j in range(m):
            if search_str[i+j] != tag_a[j]:
                check_a = False
            if search_str[i+j] != tag_b[j]:
                check_b = False
        if check_a:
            a_index.append(i+1)
        if check_b:
            b_index.append(i+1)
    for i in range(len(a_index)):
        if a_index[i]+m == b_index[i]:
            print('<blank>')
        else:
            print(search_str[a_index[i]+m-1:b_index[i]-1])
if __name__ == "__main__":
    solve()
