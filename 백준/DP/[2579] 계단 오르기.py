#https://www.acmicpc.net/problem/2579
#아 진짜 DP는 어렵다.. 어떤 식으로 코드를 짜야할 지 감이 오질 않는다..
#더 공부해야겠다..

#코드 답안#
N = int(input())

arr = []
dp = []
for i in range(N):
    arr.append(int(input()))

dp.append(arr[0])
dp.append(max(arr[0]+arr[1],arr[1]))
dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))

for i in range(3,N):
    dp.append(max(dp[i-3]+arr[i-1]+arr[i],dp[i-2]+arr[i]))
print(dp.pop())
