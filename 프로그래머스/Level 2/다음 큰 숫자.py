//https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3

def solution(n):
    answer = 0
    one_cnt = str(bin(n)).count('1')
    
    while True:
        n += 1
        if one_cnt == str(bin(n)).count('1'):
            answer = n
            break
    return answer
