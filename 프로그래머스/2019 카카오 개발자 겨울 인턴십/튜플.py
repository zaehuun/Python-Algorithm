//https://programmers.co.kr/learn/courses/30/lessons/64065
//풀고 답을 검색해보니 그 사람들이 어떻게 풀었는지 이해도 안 된다
//1점 얻은 거 보니 효율성이 내 코드는 최악인 거 같다
//최대 원소가 100000인데 이중 루프를 돌렸으니 걍 겨우 턱걸이로 통과한듯하다 

def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    tmp = []
    for i in s:
        tmp.append(list(map(int,i.split(','))))
    
    tmp.sort(key=lambda x : len(x))
    
    
    for i in tmp:
        for j in range(len(i)):
            if i[j] not in answer:
                answer.append(i[j])
    return answer
