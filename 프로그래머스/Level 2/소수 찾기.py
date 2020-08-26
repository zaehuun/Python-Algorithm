//https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

import itertools
import math

def prime(num):
    a = int(math.sqrt(num))
    if num <= 1:
        return False

    for i in range(2, a+1):
        if num % i == 0:
            return False
    return True
def solution(numbers):
    answer = 0
    tmp = []
    for i in range(1, len(numbers) + 1):
        tmp += [int(''.join(k)) for k in list(itertools.permutations(numbers,i))]

    tmp = set(tmp)
    for i in tmp:
        if prime(i):
            answer += 1
    
    
    return answer
