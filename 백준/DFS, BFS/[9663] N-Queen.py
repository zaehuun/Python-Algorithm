#https://www.acmicpc.net/problem/9663

N = int(input())

arr = [0] * N

answer = 0

def promising(x):
    for i in range(x):
        if arr[i] == arr[x] or (x - i) == abs(arr[i]-arr[x]):
            return False
    return True

def chess(count):
    global answer
    if count == N:
        answer += 1
        return
    
    for i in range(N):
        arr[count] = i
        if promising(count):
            chess(count + 1)
chess(0)
print(answer)
