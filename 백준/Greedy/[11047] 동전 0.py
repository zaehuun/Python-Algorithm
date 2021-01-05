#https://www.acmicpc.net/problem/11047
#입력 n개의 수를 안 보고 걍 이중 루프를 돌려서 풀었다.
#시간초과가 떠서 O(n)으로 고쳐서 다시 풀었다.

N, K = map(int,input().split())

coin = []

for i in range(N):
    coin.append(int(input()))


result = 0

coin.reverse()

for i in coin:

    result = result + K // i
    K = K - K // i * i

print(result)
