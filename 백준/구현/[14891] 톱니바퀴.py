#https://www.acmicpc.net/problem/14891
#문제를 잘못이해해서 막혔었다..
#톱니바퀴를 돌리고 난 후에 값과 옆에 있는 톱니의 바퀴를 비교하는 게 아닌데
#코드를 짜다보니 그렇게 작성했었다..



from collections import deque

ac = [deque(input()) for _ in range(4)]
k = int(input())

while k:
    num, rotate = map(int,input().split())
    num -= 1 # 0번 부터 시작하기에..

    tmp6 = ac[num][6] #왼쪽
    tmp2 = ac[num][2] #오른쪽

    ac[num].rotate(rotate)
    tmprotate = rotate
    right = num + 1
    while right < len(ac): #선택한 톱니 기준 오른쪽
        if tmp2 != ac[right][6]:
            tmp2 = ac[right][2]
            ac[right].rotate(tmprotate * -1)
            tmprotate = tmprotate * -1
            right += 1
        else:
            break

    left = num -1
    tmprotate = rotate
    while left >= 0: #선택한 톱니 기준 왼쪽
        if tmp6 != ac[left][2]:
            tmp6 = ac[left][6]
            ac[left].rotate(tmprotate * -1)    
            tmprotate = tmprotate * -1
            left -= 1
        else:
            break

    

    k -= 1

answer = 0
for i in range(4):
    if ac[i][0] == '1':
        answer = answer + pow(2,i)

print(answer)
