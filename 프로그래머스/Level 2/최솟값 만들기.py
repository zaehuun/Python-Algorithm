//https://programmers.co.kr/learn/courses/30/lessons/12941?language=python3

def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort()
    B.reverse()
    
    for i, j in zip(A,B):
        answer = answer + i * j

    return answer
