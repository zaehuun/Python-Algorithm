def bin_search(a, target, st, end):
    print(a)
    if st > end:
        return None
    mid = (st+end) // 2 # n = 5 => st=0 end=4 -> 2
                        #@ @ (@) @ @
    if a[mid] == target: #target find!
        return mid
    elif a[mid] > target:
        return bin_search(a,target,st,mid-1)
    else:
        return bin_search(a,target,mid+1,end)


a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = bin_search(a,30,0,len(a)-1)
if result == None:
    print("fail")
else:
    print(result+1)
