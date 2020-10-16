//https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    a = ''
    while n:
        a = str(n%3) + a
        n = n//3
    for i in range(len(a)):
        answer += pow(3,i) * int(a[i])
    return answer
