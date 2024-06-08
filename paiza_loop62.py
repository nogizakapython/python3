n,m = map(int,input().split(' '))
array1 = list(map(int,input().split(' ')))
m_count = 0
for i in array1:
    if i == m:
        m_count += 1
print(m_count)
