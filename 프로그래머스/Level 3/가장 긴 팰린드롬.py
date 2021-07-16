def check(s):
    if len(s) < 2:
        return True
    if s == s[::-1]:
        return True
    return False
def solution(s):
    answer = 0
    for i in range(len(s),0,-1):
        for j in range(len(s)):
            tmp = s[j:j+i]
            if check(tmp):
                return len(tmp)
            if i + j > len(s):
                break
    return answer
