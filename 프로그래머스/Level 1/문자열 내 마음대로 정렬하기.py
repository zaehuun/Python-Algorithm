//https://programmers.co.kr/learn/courses/30/lessons/12915?language=python3

def solution(strings, n):
    answer = []
    strings.sort(key=lambda x: (x[n],x))
    print(strings)
    return strings
