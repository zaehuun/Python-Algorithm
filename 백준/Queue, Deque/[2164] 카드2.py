#https://www.acmicpc.net/problem/2164

from collections import deque

N = int(input())

deq = deque()

for i in range(N):
    deq.append(i+1)

drop = True
while len(deq) != 1:
    v = deq.popleft()
    if not drop:
        deq.append(v)
        drop = True
    else:
        drop = False

print(deq[0])
