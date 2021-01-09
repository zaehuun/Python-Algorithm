#https://www.acmicpc.net/problem/2841
#와 문제 이해가 잘 안돼서 8번 제출해서 풀었다..

N, P = map(int, input().split())

answer = 0

st = [[] for _ in range(7)]

for i in range(N):
    melody = list(map(int,input().split()))

    if not st[melody[0]]:
        st[melody[0]].append(melody)
        answer+=1

    else:
        if melody[1] > st[melody[0]][-1][1]:
            st[melody[0]].append(melody)
            answer += 1
        elif melody[1] == st[melody[0]][-1][1]:
            continue
        elif melody[1] < st[melody[0]][-1][1]:
            while st[melody[0]] and melody[1] < st[melody[0]][-1][1]:
                st[melody[0]].pop()
                answer += 1
            if st[melody[0]] and st[melody[0]][-1][1] == melody[1]:
                continue
            st[melody[0]].append(melody)
            answer += 1

        

print(answer)
