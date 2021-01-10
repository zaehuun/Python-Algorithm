#https://www.acmicpc.net/problem/9251
#LCS에 두 종류가 있다.
#Longest Common Subsequence과 Longest Common Substring
#잘 구분해서 풀자

a = input()
b = input()

a = list('0' + a)
b = list('0' + b)
c = [[0] * 1001 for _ in range(1001)]
for i in range(len(a)):
    for j in range(len(b)):
        if i == 0 or j == 0:
            c[i][j] = 0
            continue
        if a[i] == b[j]:
            c[i][j] = c[i-1][j-1] + 1
        else:
            if c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
print(c[len(a)-1][len(b)-1])
