//https://programmers.co.kr/learn/courses/30/lessons/12924?language=python3

def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                answer+=1
            if sum > n:
                break
    return answer
