n,m = map(int, input().split())
INF = 987654321
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0


for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


x,k = map(int, input().split())

result = graph[1][k] + graph[k][x]
if result >= INF:
    print(-1)
else:
    print(result)
