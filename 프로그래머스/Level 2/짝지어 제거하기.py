//https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3

def solution(s):
    answer = 0

    st = []
    
    for i in s:
        if not st: #empty
            st.append(i)
        else :  # not empty
            if st[-1] == i:
                st.pop()
            else:
                st.append(i)
                
    if not st:
        answer = 1
    return answer
