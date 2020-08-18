//https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    
    s = s.lower()
    s = s.split(" ")
    a = []
    for i in s:
        a.append(i.capitalize())    
    
    return ' '.join(a)
