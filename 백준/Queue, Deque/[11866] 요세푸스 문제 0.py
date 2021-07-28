#https://www.acmicpc.net/problem/11866
#1년 전에 어떻게 풀 지 몰라서 넘겼는데 좀만 생각해보니 쉽게 풀 수 있었다.
#물론 코드가 효율적인지는 잘 모르겠다.
#K번째 수를 어떻게 계속 처리할까했는데 원형 큐를 생각하니 됐다.

# from collections import deque
# N, K = map(int,input().split())
# idx = 1
# deq = deque()
# for i in range(N):
#     deq.append(i+1)
# answer = []
# while deq:
#     if idx == K:
#         answer.append(deq.popleft())
#         idx = 1
#     else:
#         deq.append(deq.popleft())
#         idx += 1
# print('<'+", ".join(map(str,answer))+'>')

# 추천 문제에 있어서 다시 풀었는데 전보다 깔끔해졌다.
from collections import deque
N, K = map(int,input().split())
deq = deque([i+1 for i in range(N)])
answer = []
while deq:
    deq.rotate(-K+1)
    answer.append(deq.popleft())
print('<'+", ".join(map(str,answer))+'>')
