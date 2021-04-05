#https://www.acmicpc.net/problem/1316
N = int(input())

def solve(S):
    check = []

    for i in S:
        if not check:
            check.append(i)
        else:
            if check[-1] == i:
                continue
            else:
                if i in check:
                    return False
                check.append(i)
    return True

answer = 0

while N:
    S = input()
    if solve(S):
        answer+=1
    N -= 1
print(answer)
    
