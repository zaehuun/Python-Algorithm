n = int(input())
member = list(map(int,input().split()))
member.sort()
#1 2 2 2 3
#1 / 2 2 /
print(member)

answer = 0
cnt = 0
for i in member:
    cnt += 1 #현재 i 멤버를 포함한 그룹 수
    if cnt == i:
        answer+=1
        cnt = 0
print(answer)
