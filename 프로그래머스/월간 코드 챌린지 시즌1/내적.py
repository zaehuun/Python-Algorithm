#https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = 0
    for i,j in zip(a,b):
        answer = answer + i * j
    return answer
