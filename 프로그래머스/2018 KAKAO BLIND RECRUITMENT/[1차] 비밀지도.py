//https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(0, n):
        answer.append( arr1[i] | arr2[i])

    a = []
    for i in answer:
        tmp = pow(2,n-1)
        st = ""
        while tmp >0:
            if tmp & i > 0:
                st += "#"
            else:
                st+= " "
            tmp = tmp >> 1
        a.append(st)
    return a

//////////////////////////////////////////////
def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2):
        tmp = i | j
        tmp = str(bin(tmp)[2:])
        if len(tmp) < n:
            tmp = '0' * (n-len(tmp)) + tmp
        tmp = tmp.replace('1','#').replace('0',' ')
        answer.append(tmp)
    
    return answer
