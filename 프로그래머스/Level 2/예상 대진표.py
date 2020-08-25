//https://programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 0

    while n:
        if a & 1:
            a = a // 2 + 1
        else :
            a = a // 2
        if b & 1:
            b = b // 2 + 1
        else:
            b = b //2
        
        answer += 1
        if a == b:
            return answer
        n -= 1
    return answer
