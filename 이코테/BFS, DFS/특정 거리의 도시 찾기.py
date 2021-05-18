from collections import deque
import sys
N, M, K , X = map(int,sys.stdin.readline().split())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    st, end = map(int,sys.stdin.readline().split())
    arr[st].append(end)
visit = [False] * (N+1)


answer= []

def bfs(idx):
    deq = deque()
    deq.append((idx,0))
    visit[idx] = True
    while deq:
        index, cnt = deq.popleft()
        if cnt == K:
            answer.append(index)
        elif cnt < K:
            for i in arr[index]:
                if not visit[i]:
                    visit[i] = True
                    deq.append((i,cnt+1))


bfs(X)
if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)
