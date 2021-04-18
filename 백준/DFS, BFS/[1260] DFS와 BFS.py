#https://www.acmicpc.net/problem/1260

from collections import deque
N, M, V = map(int,input().split())

arr = [[] for _ in range(N+1)]

for i in range(M):
    st, end = map(int,input().split())
    arr[st].append(end)
    arr[end].append(st)
for i in arr:
    i.sort()
dfs_visit = [False for _ in range(N+1)]
dfs_result = []
def dfs(start):
    dfs_result.append(start)
    dfs_visit[start] = True

    for i in arr[start]:
        if not dfs_visit[i]:
            dfs(i)
dfs(V)


bfs_visit = [False for _ in range(N+1)]
bfs_result = []
def bfs(start):
    deq = deque()
    deq.append(start)
    bfs_result.append(start)
    bfs_visit[start] = True

    while deq:
        v = deq.popleft()
        for i in arr[v]:
            if not bfs_visit[i]:
                bfs_result.append(i)
                bfs_visit[i] = True
                deq.append(i)
bfs(V)
print(" ".join(list(map(str,dfs_result))))
print(" ".join(list(map(str,bfs_result))))
