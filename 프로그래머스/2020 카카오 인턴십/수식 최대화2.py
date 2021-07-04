from itertools import permutations
def cal(a,b,op):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    else:
        return a-b
def solution(expression):
    answer = 0
    op_pm = list(permutations('+-*'))

    op = []
    nums = []
    tmp = ""
    for i in expression:
        if '0'<=i<='9':
            tmp+=i
        else:
            nums.append(int(tmp))
            op.append(i)
            tmp = ''
    nums.append(int(tmp))
    print(nums,op)
    
    for i in op_pm:
        tnum = nums[:]
        top = op[:]
        for j in i:
            while j in top:
                idx = top.index(j)
                top.pop(idx)
                result = cal(tnum[idx],tnum[idx+1],j)
                tnum[idx] = result
                tnum.pop(idx+1)
        answer = max(answer,abs(tnum[0]))
    return answer
