#https://programmers.co.kr/learn/courses/30/lessons/12913?language=python3

def solution(land):
    answer = 0

    for i in range(1,len(land)): 
        for j in range(len(land[0])):
            tmp = []
            for k in range(len(land[0])):
                if j != k:
                    tmp.append(land[i-1][k])
            land[i][j] = land[i][j] + max(tmp)
    answer = max(land[-1])
    return answer
