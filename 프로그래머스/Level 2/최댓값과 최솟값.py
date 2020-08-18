//https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    s = s.split(" ")
    s = list(map(int,s))
    return str(min(s)) + " " + str(max(s))
