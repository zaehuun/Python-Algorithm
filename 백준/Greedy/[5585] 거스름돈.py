#https://www.acmicpc.net/problem/5585

N = int(input())
N = 1000 - N
#500 100 50 10 5 1
cnt = 0
if N > 0 and N // 500:
     i = N // 500
     cnt += i
     N = N % (500 * i)

if N > 0 and N // 100:
     i = N // 100
     cnt += i
     N = N % (100 * i)

if N > 0 and N // 50:
     i = N // 50
     cnt += i
     N = N % (50 * i)

if N > 0 and N // 10:
     i = N // 10
     cnt += i
     N = N % (10 * i)

if N > 0 and N // 5:
     i = N // 5
     cnt += i
     N = N % (5 * i)

if N > 0 and N // 1:
     i = N // 1
     cnt += i
     N = N % (1 * i)

print(cnt)
