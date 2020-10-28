//https://www.acmicpc.net/problem/11724
//코테 책을 통해 좀 공부해서 그런가 금방 풀 수는 있었지만 그래도 좀 어떻게 풀어야 할 지 머리에 잘 그려지지는 않는다.
N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]
check = [False] * (N+1)

for i in range(M):
    st, end = map(int,input().split())
    arr[st].append(end)
    arr[end].append(st)
def dfs(st):
    check[st] = True

    for i in arr[st]:
        if not check[i]:
            dfs(i)
cnt = 0

for i in range(1,N+1):
    if not check[i]:
        cnt += 1
        dfs(i)

print(cnt)
