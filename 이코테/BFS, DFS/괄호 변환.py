def check(s):
    st = []
    for i in s:
        if not st:
            st.append(i)
        else:
            if st[-1] == '(' and i == ')':
                st.pop()
            else:
                st.append(i)
    if st:
        return False
    return True

def solution(p):
    answer = ''
    if len(p) == 0:
        return ""
    leftCnt = rightCnt = idx = 0
    for i in range(len(p)):
        if p[i] == '(':
            leftCnt = leftCnt + 1
        elif p[i] == ')':
            rightCnt = rightCnt + 1
        
        if leftCnt != 0 and leftCnt == rightCnt:
            idx = i
            break
    u = p[:idx+1]
    #print(u,p[idx+1:])
    if check(u):
        return u + solution(p[idx+1:])
    s = '(' + solution(p[idx+1:]) + ')'
    
    u = u[1:len(u)-1]
    tmp = ""
    for i in u:
        if i == ')':
            tmp = tmp + '('
        else:
            tmp = tmp + ')'
    return s + tmp
