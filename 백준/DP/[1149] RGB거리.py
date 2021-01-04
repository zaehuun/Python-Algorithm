#https://www.acmicpc.net/problem/1149
#DP 문제를 너무 안 풀었던 거 같다..
#DP 기본 문제라는대 어떤 식으로 코드 구조를 작성해야할지 감이 오질 않았다.
#앞으로 DP 문제도 많이 풀어야겠다.

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(1001)]

for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + arr[i-1][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + arr[i-1][1]
    dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + arr[i-1][2]

print(min(dp[N]))

