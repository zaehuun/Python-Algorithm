#https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = []
    r = 0
    d = 0
    while s != "1":
        d += s.count('0') #지워야 할 0의 수
        s = s.replace('0','') #0 제거
        
        length = len(s)
        
        s = bin(length)[2:]
        r += 1
        
    answer.append(r)
    answer.append(d)
    return answer
