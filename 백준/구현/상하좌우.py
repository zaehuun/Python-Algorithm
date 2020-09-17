n = int(input())
a = input().split()
st = [1,1]
for i in a:
    s1 = st[0]
    s2 = st[1]
    if i == 'R':
        s2 += 1
    elif i == 'L':
        s2 -= 1
    elif i == 'U':
        s1 -= 1
    elif i == 'D':
        s1 += 1
    
    if s1 > 0 and s2 > 0 and s1 <= n and s2 <= n:
        st[0] = s1
        st[1] = s2
print(st)
