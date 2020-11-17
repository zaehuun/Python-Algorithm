//https://www.acmicpc.net/problem/1764
//문제 이름 때문에 풀었다.
//N과 M이 최대 500000이라 합치면 1000000이다.
//예전 같았으면 2중 반복문 돌면서 체크 했을텐데 요즘은 딕셔너리를 자주 써서 O(N+M) 정도로 푼 거 같다.

N, M = map(int, input().split())

names = dict()
answer = []
for i in range(N+M):
    name = input()

    if name in names:
        answer.append(name)
    else:
        names[name] = 1
print(len(answer))
answer.sort()

for i in answer:
    print(i)
