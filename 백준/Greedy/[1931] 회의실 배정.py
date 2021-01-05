#https://www.acmicpc.net/problem/1931
#가끔은 주입식 교육이 좋을 때도 있구나 싶다.
#알고리즘 수업 들을 때 그리디는 회의 종료 시간을 기준으로 풀면 된다는 말만 기억나서 풀었다.

N = int(input())
time = [list(map(int,input().split())) for _ in range(N)]
#print(time)
time.sort(key=lambda x: (x[1],x[0]))


end = 0
result = 0
for i in time:
    if i[0] >= end:
        #print(i[0],i[1])
        #print(i[1],end)
        end = i[1]
        result+=1

print(result)
