//https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3

from itertools import combinations
import math

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if(num % i ==0):
            return False
        
    return True;

def solution(nums):
    answer = 0

    a = list(combinations(nums,3))
    
    for item in a:
        if(isPrime(sum(item))):
            answer+=1

    return answer
