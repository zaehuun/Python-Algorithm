//답안 코드는 되게 간단한데 너무 복작하게 풀었다.

n = int(input())
member = list(map(int,input().split()))
member.sort()
#1 2 2 2 3
#1 / 2 2 /
print(member)

answer = 0
idx = 0
while idx < len(member):
    cnt = 1
    val = member[idx]
    print(idx,val)
    if cnt == val:
        answer+=1
        idx+=1
        continue
    else:
        if val > len(member[idx+1:]):
            break
        while cnt != val:
            cnt+=1
        idx += cnt
        answer+=1
        
print(answer)
