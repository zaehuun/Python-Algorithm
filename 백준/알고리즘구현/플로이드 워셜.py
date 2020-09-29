INF = 987654321
#노드 수 및 간선 수
n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = 0

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1, n+1):
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

for a in range(1,n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print("x",end=" ")
        else:
            print(graph[a][b], end=' ')
    print()
