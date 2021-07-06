#첫 코드
#2차원 배열을 만들고 다 돌면서 진행을 하니 시간 초과가 떴다..
#그래서 연결된 노드만 추가할 수 있도록 수정하니 시간초과 해결
from collections import deque
def bfs(start,visit,arr):
    cnt = 0
    v = 0
    deq = deque()
    deq.append((start,0))
    while deq:
        st, n = deq.popleft()
        if n > v:
            cnt = 0
            v = n
        if n == v:
            cnt += 1
        for idx in range(len(arr[st])):
            if arr[st][idx] == 1 and not visit[idx]: #연결되어있고 아직 방문 x
                visit[idx] = True
                deq.append((idx,n+1))
    return cnt

def solution(n, edge):
    answer = 0
    visit = [False] * n
    visit[0] = True
    arr = [[0] * n for _ in range(n)]
    for st,end in edge:
        arr[st-1][end-1] = 1
        arr[end-1][st-1] = 1
    answer = bfs(0,visit,arr)
    return answer


#시간 초과 해결한 문제
from collections import deque
def bfs(start,visit,arr):
    cnt = 0
    v = 0
    deq = deque()
    deq.append((start,0))
    while deq:
        st, n = deq.popleft()
        if n > v:
            cnt = 0
            v = n
        if n == v:
            cnt += 1
        for idx in arr[st]:
            if not visit[idx]:
                visit[idx] = True
                deq.append((idx,n+1)) 
    return cnt

def solution(n, edge):
    answer = 0
    visit = [False] * n
    visit[0] = True
    arr = [[]  for _ in range(n)]
    for st,end in edge:
        arr[st-1].append(end-1)
        arr[end-1].append(st-1)
    answer = bfs(0,visit,arr)
    return answer
