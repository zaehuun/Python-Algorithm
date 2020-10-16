https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    '''
    1
    2  9
    3 10 8
    4  5 6 7
    
    '''
    tmp = []
    answer = [[0] * n for _ in range(n)]
    x = -1
    y = 0
    
    num = 1
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0 :
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
            
    for i in range(n):
        for j in range(n):
            if answer[i][j] != 0 :
                tmp.append(answer[i][j])
                
    return tmp
