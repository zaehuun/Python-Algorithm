#https://www.acmicpc.net/problem/12789

N = int(input())

line = list(map(int,input().split()))

wait = []

num = 1

while line:
    v = line.pop(0)
    if v == num:
        num += 1
    else:
        wait.append(v)

    while wait and wait[-1] == num:
        wait.pop()
        num += 1

if not wait:
    print("Nice")
else:
    print("Sad")
