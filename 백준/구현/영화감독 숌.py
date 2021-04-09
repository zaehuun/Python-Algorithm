#https://www.acmicpc.net/problem/1436

N = int(input())

s = 666

def find666(v):
    flag = 0
    v = str(v)
    for i in v:
        if i == '6':
            flag += 1
            if flag == 3:
                return True
        else:
            flag = 0
while N:
    if find666(s):
        N -= 1
    s += 1

print(s-1)


