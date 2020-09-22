def bin_search(a, target, st, end):

    while st <= end:
        print(a[st:end+1])
        mid = (st + end) // 2
        if a[mid] == target:
            return mid
        elif a[mid] > target:
            end = mid-1
        else:
            st = mid + 1
    return None


a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = bin_search(a,2,0,len(a)-1)
if result == None:
    print("fail")
else:
    print(result+1)
