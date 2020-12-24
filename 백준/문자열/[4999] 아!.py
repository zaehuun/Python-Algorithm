#https://www.acmicpc.net/problem/4999
#정답 비율이 63퍼 문제


a = input()
b = input()

if len(a) >= len(b) and b in a:
    print("go")
else:
    print("no")
