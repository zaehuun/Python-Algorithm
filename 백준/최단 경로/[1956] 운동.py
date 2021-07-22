# v, e  = map(int,input().split())
# arr = [[987654321] * v for _ in range(v)]
# for _ in range(e):
#     st, end, cost = map(int,input().split())
#     arr[st-1][end-1] = cost
# min_v = 987654321
# for k in range(v):
#     for i in range(v):
#         for j in range(v):
#             if arr[i][j] > arr[i][k] + arr[k][j]:
#                 arr[i][j] = arr[i][k] + arr[k][j]

# for i in range(v):
#     min_v = min(min_v,arr[i][i])

# if min_v:
#     print(min_v)
# else:
#     print(-1)

위 코드처럼 마지막에 for문을 또 돌지 않고 풀고 싶었다. 부캠 끝나고 자기 전까지 그냥 머리 속으로 생각해봤는데 3중 for문 안에서 i->j와 j->i를 체크해주면 될 거 같았다.
그래서 아래처럼 코드를 변경 했다. 비록 조건문이 좀 더럽지만...
v, e  = map(int,input().split())
arr = [[987654321] * v for _ in range(v)]
for _ in range(e):
    st, end, cost = map(int,input().split())
    arr[st-1][end-1] = cost
min_v = 987654321
for k in range(v):
    for i in range(v):
        for j in range(v):
            if arr[i][k] == 987654321:
                continue
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
            if arr[i][j] != 987654321 and arr[j][i] != 987654321:
                if arr[i][j] and arr[j][i]:
                    min_v = min(min_v,arr[i][j]+arr[j][i])
if min_v!=987654321:
    print(min_v)
else:
    print(-1)
