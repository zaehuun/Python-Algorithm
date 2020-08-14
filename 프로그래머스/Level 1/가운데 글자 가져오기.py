//https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3

def solution(s):
    answer = ''
    l = len(s)
    if l % 2 == 0:
        answer = s[int(l/2)-1 : int(l/2) +1]
    else:
        answer = s[int(l/2)]
    return answer
