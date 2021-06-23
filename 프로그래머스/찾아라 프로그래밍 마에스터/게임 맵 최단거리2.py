from collections import deque
def solution(maps):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append((0,0,1))
    row = len(maps)
    col = len(maps[0])
    while q:
        x, y, cnt = q.popleft()
        if x == row -1 and y == col - 1:
            return cnt
        
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if -1<tx<row and -1<ty<col and maps[tx][ty] == 1:
                maps[tx][ty] = cnt + 1
                q.append((tx,ty,cnt+1))
    print(maps)
    return -1
