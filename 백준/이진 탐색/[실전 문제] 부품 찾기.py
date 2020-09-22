//데이터 수가 n은 최대 1000000, m은 최대 100000
//선형 탐색으로 찾으면 O(n*m)이려나 암튼 엄청 커짐
//이진 탐색으로 하면 O(m * logn) 정도 나올까..

def bin_search(a, target, st, end):
    if st > end:
        return None
    
    mid = (st + end) // 2

    if a[mid] == target:
        return mid
    elif a[mid] > target:
        return bin_search(a,target,st,mid-1)
    else:
        return bin_search(a, target,mid + 1, end)

n = int(input())
boo = list(map(int,input().split()))
boo.sort() #이진 탐색은 정렬 필요
m = int(input())
pil = list(map(int,input().split()))

for x in pil:
    result = bin_search(boo,x,0,n-1)
    if result != None:
        print("yes",end=' ')
    else:
        print("no",end=' ')
