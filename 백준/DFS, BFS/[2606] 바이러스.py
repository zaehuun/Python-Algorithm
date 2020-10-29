//https://www.acmicpc.net/problem/2606

n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]
check = [0] * (n+1)

for i in range(m):
    st, end = map(int,input().split())
    arr[st].append(end)
    arr[end].append(st)

answer = 0

def dfs(i):
    global answer
    check[i] = 1

    for j in arr[i]:
        if not check[j]:
            answer += 1
            dfs(j)

dfs(1)

print(answer)
