//https://programmers.co.kr/learn/courses/30/lessons/17686#
//cmp함수는 funtools 사용해보려고 짜본건데 lambda랑 시간 비교해보니 역시 내가 짠 코드는 확실히 느리다
//존재하는 것들을 사용하는게나은거같다...
//re.split()에서 ([0-9]+)를 하면 숫자 포함, () 없으면 숫자 미포함
import re

'''def cmp(a,b):
    if a[0].lower() == b[0].lower() and int(a[1]) == int(b[1]):
        return 0
    else:
        if a[0].lower() < b[0].lower():
            return -1
        elif a[0].lower() > b[0].lower():
            return 1
        else:
            if int(a[1]) < int(b[1]):
                return -1
            elif int(a[1]) > int(b[1]):
                return 1
            else:
                return 0
''' #이건 걍 함 짜본 함수

def solution(files):
    answer = []

    r = re.compile("[0-9]+")
    div = []

    for i in files:
        div.append(re.split("([0-9]+)",i))

    answer = sorted(div,key=lambda x : (x[0].lower(), int(x[1])))
    answer = [''.join(i) for i in answer]
    return answer
