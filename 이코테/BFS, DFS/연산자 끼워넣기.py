import sys
N = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

# print(nums)
# print(visit)
op = list(map(int,sys.stdin.readline().split()) )
#pc : + , mc : -, mpc : *, dc : /
# print(pc,mc,mpc,dc)

max_answer = -987654321
min_answer = 987654321

total = 0

def solve(idx,cnt,total):
    global min_answer, max_answer
    if cnt == N-1:
        min_answer = min(total, min_answer)
        max_answer = max(total, max_answer)

    else:
        if op[0]:
            op[0] -= 1
            solve(idx + 1, cnt + 1, total + nums[idx])
            op[0] += 1
        if op[1]:
            op[1] -= 1
            solve(idx + 1, cnt + 1, total - nums[idx])
            op[1] += 1
        if op[2]:
            op[2] -= 1
            solve(idx + 1, cnt + 1, total * nums[idx])
            op[2] += 1
        if op[3]:
            op[3] -= 1
            solve(idx + 1, cnt + 1, int(total / nums[idx]))
            op[3] += 1
                


solve(1,0,nums[0])
print(max_answer,min_answer)
