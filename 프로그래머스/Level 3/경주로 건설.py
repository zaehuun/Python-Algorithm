#아 진짜 개어렵다 뭔 생각으로 맨 처음에 dfs로 풀려했지
#그리고 무슨 생각으로 이전 방향과 전전방햑까지넘겨서 수직을 체크하려했지..

from collections import deque
def valid(x,y,n):
    if -1 < x < n and -1 < y < n:
        return True
    return False
def solution(board):
    answer = 0
    deq = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    #down, up, right, left
    costs=[[987654321] * len(board[0]) for _ in range(len(board[0]))]
    if board[0][1] == 0:
        deq.append((0,1,2,100))
        costs[0][1] = 100
    if board[1][0] == 0:
        deq.append((1,0,0,+100))
        costs[1][0] = 100

    while deq:
        # print(deq)
        x,y,dir,cost = deq.popleft()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
                #유효 범위                      아직 미방문
            if not valid(tx,ty,len(board[0])):
                continue
            if board[tx][ty]: # 벽일 때
                continue
            if dir == i: #같은 방향
                ncost = 100
            else:
                ncost = 600
            now_cost = ncost + cost
            if now_cost <= costs[tx][ty]:
                costs[tx][ty] = now_cost
                deq.append((tx,ty,i,now_cost))

    
    return costs[len(board[0])-1][len(board[0])-1]
