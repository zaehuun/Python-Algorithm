//https://www.acmicpc.net/problem/3986

n = int(input())
cnt = 0
while n:
    arr = input()

    tmp = []
    
    for i in range(0, len(arr)):
        if not tmp:
            tmp.append(arr[i])
        else:
            if tmp[-1] == arr[i]:
                tmp.pop()
            else:
                tmp.append(arr[i])

    if not tmp:
        cnt += 1
    n -= 1

print(cnt)
