//https://www.acmicpc.net/problem/2941
//매우 간단한 문제였는데 답을 보고 띠용..
//index 에러 날까봐 걱정했는데 이렇게 풀면 전혀 걱정할게없었다..

dic = ["c=","c-","dz=","d-","lj","nj","s=","z="]

croa = input()

for i in dic:
    if i in croa:
        croa = croa.replace(i,"*")


print(len(croa))
