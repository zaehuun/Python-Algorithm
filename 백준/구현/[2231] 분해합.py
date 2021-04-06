#https://www.acmicpc.net/problem/2231
#flag 두는게 별로 깔끔해보이진 않았는데 찾아보니 깔끔하게 풀 수 있었구나

N = int(input())
num = 1
answer =987654321
flag = False
while num <= N:
    v = num + sum(map(int,list(str(num))))
    if v == N:
        if answer > num:
            answer = num
            flag = True
            break
    num+=1
if flag:
    print(answer)
else:
    print(0)
    
    
############
#인터넷 코드
num = int(input())
answer = 0

for i in range(1, num+1):
    coef_num_list = list(map(int, str(i)))
    answer = i + sum(coef_num_list)
    
    if answer == num:
        print(i)
        break

    if i == num:
        print(0)
