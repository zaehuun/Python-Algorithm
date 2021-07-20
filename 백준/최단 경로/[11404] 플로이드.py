n = int(input()) #도시 수
m = int(input()) #버스 수

arr = [[987654321] * n for _ in range(n)]

for _ in range(m):
    st, end, cost = map(int,input().split())
    if arr[st-1][end-1] > cost:
        arr[st-1][end-1] = cost

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

arr = [[0 if j == 987654321 else j for j in i ] for i in arr]
for i in arr:
    for j in i:
        print(j, end=' ')
    print()
