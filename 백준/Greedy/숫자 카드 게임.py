
N, M = map(int, input().split())


a = [list(map(int,input().split())) for _ in range(N)]

answer = 0

for i in a:
    v = min(i)
    answer = max(answer,v)

print(answer)
