//알고리즘 수업 들을 때 반복문으로 적힌 코드보고 정 떨어졌었는데
//재귀로 짠 코드 보니 이해도 잘 되고 좋다

def recur_quicksort(a):
    if len(a) <= 1:
        return a
    equal = []
    big = []
    small = []

    pivot = a[len(a)//2]

    for i in a:
        if i > pivot:
            big.append(i)
        elif i < pivot:
            small.append(i)
        else:
            equal.append(i)
    
    return recur_quicksort(small) + equal + recur_quicksort(big)


a = [1,5,3,2,7,8,9,4,1,6,8,0,10,23,6,5,44,7,22,23]
a = recur_quicksort(a)
print(a)
