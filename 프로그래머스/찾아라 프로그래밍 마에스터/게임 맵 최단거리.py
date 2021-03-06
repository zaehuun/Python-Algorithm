#https://programmers.co.kr/learn/courses/30/lessons/1844

def solution(maps):
    answer = 0
    
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    #시작
    sx = 0 
    sy = 0
    
    ex = len(maps)-1
    ey = len(maps[0])-1
    
    
    
    #초기
    queue = [(sx,sy, 1)]
    maps[sx][sy] = 0

    
    while queue:
        x, y, cnt = queue.pop(0)
        if x == ex and y == ey:
            return cnt
        
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            
            if -1 < tx <= ex and -1 < ty <= ey and maps[tx][ty]:
                maps[tx][ty] = 0
                queue.append((tx,ty,cnt+1))

    return -1
