#https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    while n:
        a = n // 3
        b = n % 3
        if b == 0:
            b = 4
            n = n // 3 - 1
        else:
            n = n // 3

        answer = str(b) + answer
    return answer
