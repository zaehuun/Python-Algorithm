def check(s):
    st = []
    li = ['}',')',']']
    dic = {'}' : '{',  ']': '[', ')' : '('}
    for i in s:
        if not st:
            st.append(i)
        else:
            if i in li and dic[i] == st[-1]:
                st.pop()
            else:
                st.append(i)
    if not st:
        return True
    else:
        return False
            
def solution(s):
    #s in consist of [ { (
    s = list(s)
    answer = 0
    for _ in range(len(s)):
        if check(s):
            answer += 1
        s.append(s.pop(0))
    return answer
