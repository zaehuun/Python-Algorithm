N = int(input())

arr = list(map(int,input().split()))
arr.sort()
print(arr)

answer = 0 #총 그룹
num = 0 #현재 그룹 X명
for i in arr: # 1 2 2 2 3
    num = num + 1
    if num == i: #현재 그룹 공포 인원이랑 멤버 공포도가 일치
        answer = answer + 1
        num = 0
    #else:
        #num = num + 1
        #뭐 있나

print(answer)
