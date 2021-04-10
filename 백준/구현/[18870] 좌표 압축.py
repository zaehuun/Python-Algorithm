#https://www.acmicpc.net/problem/18870

import copy
N = int(input())

arr = list(map(int,input().split()))
tmp = copy.deepcopy(arr)
arrSorted = sorted(list(set(tmp)),reverse=True)
answer = []

dic = dict()
for i in range(len(arrSorted)):
    dic[arrSorted[i]] = len(arrSorted) - i - 1
for i in arr:
    print(dic[i],end=" ")
