import sys
N = int(sys.stdin.readline())
arr1 = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))

arr1.sort()
dic = {}
answer = []

def binary(arr1,num):
    left = 0
    right = len(arr1) - 1
    while left<=right:
        mid = (left+right) // 2
        if arr1[mid] == num:
            cnt = arr1[left:right+1].count(num)
            return cnt
        if arr1[mid] > num:
            right = mid - 1
        else:
            left = mid + 1

    return 0

for num in arr2:
    if num not in dic:
        dic[num] = binary(arr1,num)

print(' '.join(str(dic[x])  for x in arr2))
#-10 -10 2 3 3 6 7 10 10 10
