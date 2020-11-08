//https://www.acmicpc.net/problem/10451
case = int(input())

while case>0:
    answer = 0
    N = int(input())
    tmp = [[0]]
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        tmp.append(arr[i])

    visit = set()

    def dfs(x):
        
        visit.add(x)
        a = tmp[x]
        if a not in visit:
            dfs(a)

    for i in range(1, len(tmp)):
        if i not in visit:
            dfs(i)
            answer += 1

    print(answer)

    case -= 1
