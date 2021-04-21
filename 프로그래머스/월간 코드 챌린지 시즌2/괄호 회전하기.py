#https://programmers.co.kr/learn/courses/30/lessons/76502?language=python3
#변수명을 좀 제대로 정해야겠다. 막 정하다보니 같은 변수명을 쓰고 있어서 값이 깨지고 막 그런다.
dic = {']' : '[', ')' : '(', '}' : '{'}
def check(st):
    stack = []
    for s in st:
        if not stack or s == '[' or s == '(' or s == '{':
            stack.append(s)
        else:
            if stack[-1] == dic[s]:
                stack.pop()
            else:
                stack.append(s)
    if stack:
        return False
    return True
def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)-1):
        if check(''.join(s)):
            answer += 1
        s.append(s.pop(0))

    return answer
