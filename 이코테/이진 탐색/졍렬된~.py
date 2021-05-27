from bisect import bisect_left, bisect_right

N, x = map(int,input().split())
arr = list(map(int,input().split()))

left = bisect_left(arr,x)
right = bisect_right(arr,x)

answer = right-left
if not answer:
    print(-1)
else:
    print(right-left)
