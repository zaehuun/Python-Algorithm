n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(len(arr[i])):
        left = right = 0
        if j == 0:
            left = 0
        else:
            left = arr[i-1][j-1]
        
        if j == len(arr[i]) - 1:
            right = 0
        else:
            right = arr[i-1][j]

        arr[i][j] = arr[i][j] + max(left,right)

print(max(arr[n-1]))
