#https://www.acmicpc.net/problem/12789
#반복분 1 loop 안에 꼭 처리를 하나만 할 필요는 없다.

#처음 코드
N = int(input())

line = list(map(int,input().split()))

wait = []

num = 1

while line:
    if line[0] == num:
        line.pop(0)
        num += 1
    else:
        while line and num != line[0]:
            wait.append(line.pop(0))
    while wait and wait[-1] == num:
        wait.pop()
        num += 1

if not wait:
    print("Nice")
else:
    print("Sad")
    
    
    
   
#인터넷 보고 고친 코드

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
