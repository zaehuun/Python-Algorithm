//https://programmers.co.kr/learn/courses/30/lessons/17677
//맨 첨에 정규식을 사용했는데 앚기 사용법이 미숙하여 문제에 딱 맞게 적용을 못 했다
//isalpha라는 함수가 있어서 사용해봤다.
//"aa"는 True를, "a+"는 False를 return 해준다.
def solution(str1, str2):
    answer = 0
    
    st1 = []
    st2 = []
    
    for i in range(0, len(str1)-1):
        if ''.join(str1[i:i+2]).isalpha():
            st1.append(''.join(str1[i:i+2]).lower())
    for i in range(0, len(str2)-1):
        if ''.join(str2[i:i+2]).isalpha():
            st2.append(''.join(str2[i:i+2]).lower())
    print(st1)
    print(st2)
    gyo = []
    for i in st1:
        if i in st2:
            gyo.append(i)
            st2.pop(st2.index(i))
    
    st1 = st1 + st2
    if len(st1) == 0:
        return 65536
    return int(len(gyo) / len(st1) * 65536)
