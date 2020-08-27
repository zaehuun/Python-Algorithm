//https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
//처음엔 permutations 사용해서 모든 경우의 수 구해서 했는데 시간 초과가 떴다
//c++에서는 cmp 함수를 맘대로 지정할 수 있었는데 python에서는 없을까 해서 찾아보니 있긴 했다
//좀 다르지만 왼쪽이 더 먼저 오게 하려면 -1, 그대로 0, 오른쪽이 먼저 오게는 1
//functools.cmp_to_key

import functools
def cmp (a,b):
    if a + b >= b + a:
        return -1
    else:
        return 1
    
def solution(numbers):

    if sum(numbers) == 0:
        return "0"
    
    numbers = [str(i) for i in numbers]
    
    numbers = sorted(numbers, key=functools.cmp_to_key(cmp))
    return ''.join(numbers)
