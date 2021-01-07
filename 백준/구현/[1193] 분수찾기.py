#https://www.acmicpc.net/problem/1193
#복학하고 처음 코테 문제 풀어보려고 했을 때 포기한 문제였는데
#지금와서 좀 생각해서 푸니 충분히 풀 수 있던 문제였다.


N = int(input())
v = 1
while True:
    if N - v <= 0:
        break
    N -= v
    v+=1
v = v + 1
N = N -1 
#print(v,N)
p = 0
c = 0

if v & 1:
    c = 1
    p = v - 1

    print(''.join([str(c + N),'/' ,str(p - N)]))
    
else:
    p = 1
    c = v - 1

    print(''.join([str(c - N),'/', str(p + N)]))

