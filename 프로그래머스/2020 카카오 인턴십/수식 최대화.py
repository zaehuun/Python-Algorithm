//https://programmers.co.kr/learn/courses/30/lessons/67257
//인덱스 계산이 좀 약한 거 같다.
//항상 인덱스 계산이 제대로 되는지 확인하려면 볼펜으로 적어가면서 확인하는데 머리로만 생각해봐야겠다.

from itertools import permutations
import re
def calc(a,b,op):
    if op == "+":
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)
    
def solution(expression):
    ops = list(permutations("+-*"))
    #print(ops)
    a = re.compile("\D")
    op = a.findall(expression)
    #print(op)
    
    a = re.compile("[0-9]+")
    num = a.findall(expression)
    #print(num)
    answer = 0
    tmp = []
    for i in ops: #[*,-,+] 우선순위
        tmpop = op[:]
        tmpnum = num[:]
        for j in i: #*,-,+
            while j in tmpop:
                idx = tmpop.index(j)
                tmpnum[idx] = calc(tmpnum[idx],tmpnum[idx+1],j)
                tmpop.pop(idx)
                tmpnum.pop(idx+1)
        tmp.append(abs(sum(list(map(int,tmpnum)))))
    #print(tmp)
    answer = max(tmp)
    return answer
