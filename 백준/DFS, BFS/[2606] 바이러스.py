//https://www.acmicpc.net/problem/2606

answer = 0
N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
check = [False for _ in range(N+1)]

for i in range(M):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
def dfs(idx):
    global answer
    check[idx] = True

    for i in arr[idx]: #[2,5]
        if check[i] == False:
            answer += 1
            dfs(i)

dfs(1)
print(answer)
