#https://www.acmicpc.net/problem/14888
#조금은 성장한걸까...★

N = int(input())
numbers = list(map(int,input().split()))
op = list(map(int,input().split()))


min_answer = 987654321
max_answer = -987654321


def push_op(idx,cnt, total):
    global min_answer, max_answer
    if cnt == N-1:
        min_answer = min(total, min_answer)
        max_answer = max(total, max_answer)

    else:
        if op[0]:
            op[0] -= 1
            push_op(idx + 1, cnt + 1, total + numbers[idx])
            op[0] += 1
        if op[1]:
            op[1] -= 1
            push_op(idx + 1, cnt + 1, total - numbers[idx])
            op[1] += 1
        if op[2]:
            op[2] -= 1
            push_op(idx + 1, cnt + 1, total * numbers[idx])
            op[2] += 1
        if op[3]:
            op[3] -= 1
            push_op(idx + 1, cnt + 1, int(total / numbers[idx]))
            op[3] += 1


push_op(1,0,numbers[0])
print(max_answer)
print(min_answer)
