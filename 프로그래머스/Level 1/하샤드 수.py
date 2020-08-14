//https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3

c++스럽게
def solution(x):
    answer = True

    tmp = x
    sum = 0
    while(tmp>0):
        sum = sum + tmp%10
        tmp = int(tmp/ 10)
    if(x % sum != 0 ):
        return False
    return answer
    
python스럽게
def solution(x):
    
    a = str(x)
    a = list(map(int,list(a)))
    return x % sum(a) == 0
