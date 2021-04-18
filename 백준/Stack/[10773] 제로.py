k = int(input())
st = []

for i in range(k):
    v = int(input())
    if  v == 0:
        st.pop()
    else:
        st.append(v)

print(sum(st))
