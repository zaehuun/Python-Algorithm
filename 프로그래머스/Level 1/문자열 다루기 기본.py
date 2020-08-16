//https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3

def solution(s):
    return s.isdigit() and (len(s) == 6 or len(s) == 4)
