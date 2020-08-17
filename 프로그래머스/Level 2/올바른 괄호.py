//https://programmers.co.kr/learn/courses/30/lessons/12909?language=python3


def solution(s):
    answer = True
    st = []
    
    for i in s:
        if i == "(":
            st.append(i)
        else:
            if not st:
                return False
            elif st[-1] == "(":
                st.pop()
    if st:
        return False

    return True
