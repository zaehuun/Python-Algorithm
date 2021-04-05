#https://www.acmicpc.net/problem/1065
#나름대로 신기하게 풀었다고 생각하고 정답을 봤는데
#a[0] - a[1] == a[1] - a[2] 이렇게 하는 거 보고 현타오네
#최대 999라서 정말 그렇게 해도 됐는데 문제에서 제공하는 힌트들을 제대로 활용하지못하는거같다.

X = int(input())

num = 1
answer = 0
while num <= X:
    v = str(num)

    if len(v) <= 2:
        answer += 1
    else:
        s = set()
        for i in range(len(v)-1):
            s.add(int(v[i]) - int(v[i+1]))
        if len(s) == 1:
            answer +=1
    num += 1
print(answer)
