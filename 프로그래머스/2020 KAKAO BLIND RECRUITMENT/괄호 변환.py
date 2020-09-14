//https://programmers.co.kr/learn/courses/30/lessons/60058
//이번 2021 카카오 1번 문제처럼 순서를 알려주는 문제다.
//이런 문제는 빨리 풀어야 되는데 인덱스만 나오면 사고가 멈춘다

def bal (u):
    if len(u) <= 1:
        return False
    return u.count('(') == u.count(')')

def right(u):
    tmp = []
    for i in u:
        if i =='(':
            tmp.append(i)
        else:
            if not tmp:
                return False
            tmp.pop()
    if tmp:
        return False
    return True

def solution(p):
    if p == '':
        return p
    if right(p):
 
        return p
    idx = 0
    #2
    for i in range(len(p)):
        if bal(p[:i+1]):
            idx = i+1
            break

    #3
    if right(p[:idx]):
        return p[:idx] + solution(p[idx:])
    else:
        tmp = '('
        tmp += solution(p[idx:])
        tmp += ')'
        u = p[:idx]
        for i in u[1:-1]:
            if i =='(':
                tmp += ')'
            else:
                tmp += '('
        return tmp
