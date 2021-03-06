#https://programmers.co.kr/learn/courses/30/lessons/49994#

def solution(dirs):
    #x,y
    dir = {'U' : [0,1], 'D' : [0,-1], 'R' : [1,0], 'L' : [-1,0]}
    
    tmp = {}
    answer = 0
    x = 0
    y = 0
    for d in dirs:
        if -6 < dir[d][0] + x < 6 and -6 < dir[d][1] + y < 6:
            if (x, y, dir[d][0] + x, dir[d][1] + y) not in tmp and (dir[d][0] + x, dir[d][1] + y, x, y) not in tmp:
                print(x,y)
                tmp[(x,y,dir[d][0] + x,dir[d][1] + y)] = 1
                tmp[(dir[d][0] + x,dir[d][1] + y,x,y)] = 1
                answer+=1
            x = dir[d][0] + x
            y = dir[d][1] + y
            #print(x,y)
            
            
    return answer
