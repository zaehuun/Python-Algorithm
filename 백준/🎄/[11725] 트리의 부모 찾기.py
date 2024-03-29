import sys
sys.setrecursionlimit(10 ** 9)

N = int(input())
answer = [0] * (N+1)
arr = [[] for _ in range(N+1)]
def dfs(root):
    for i in arr[root]:
        if answer[i] == 0:  
            answer[i] = root
            dfs(i)
for _ in range(N-1):
    p, c = map(int,input().split())
    arr[p].append(c)
    arr[c].append(p)
dfs(1)
for i in range(2,N+1):
    print(answer[i])

#       1
#     6    4
#  3     7   2
#5
#
#
