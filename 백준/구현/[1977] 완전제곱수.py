#https://www.acmicpc.net/problem/1977
#예전에 완전제곱 구분하는 문제를 푼 적이 있어서 빠르게 풀 수 있었다.
#다이나믹 프로그래밍으로 푸는 방법도 있는데 한 번 나중에 기회가 되면 풀어봐야겠다.

import math
M = int(input())
N = int(input())

answer = 0
num = 987654321
find = False
for i in range(M, N+1):
    if math.sqrt(i) % 1 == 0:
        find = True
        answer += i
        num = min(num, i)
if find:
    print(answer)
    print(num)
else:
    print(-1)
        
