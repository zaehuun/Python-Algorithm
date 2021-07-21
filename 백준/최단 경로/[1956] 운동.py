v, e  = map(int,input().split())
arr = [[987654321] * v for _ in range(v)]
for _ in range(e):
    st, end, cost = map(int,input().split())
    arr[st-1][end-1] = cost
min_v = 987654321
for k in range(v):
    for i in range(v):
        for j in range(v):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(v):
    min_v = min(min_v,arr[i][i])

if min_v:
    print(min_v)
else:
    print(-1)
