//https://programmers.co.kr/learn/courses/30/lessons/12981
//딕셔너리 이용해서 중복 단어 체크하려 했으나 그 단어는 처음 나올 때는 문제 되지 않지만
//그 다음 나올 때 문제되는데 그걸 코드로 구현하기는 좀 싫었고 너무 하드 코딩 같았다
//걍 사용된 단어 다 기록하고 확인하는 쪽으로...

def solution(n, words):
    answer = []

    used = []
    
    used.append(words[0])
    
    brek = False
    for i in range(1, len(words)):
        if used[-1][-1] == words[i][0]: # 처음 마지막 같으면
            if words[i] not in used: #중복이 아니라면
                used.append(words[i]) #사용된 리스트에 넣고
            else: #처음 마지막 같은데 중복이라면
                answer.append(i % n + 1)
                answer.append(i//n + 1)
                brek = True
                break
        else: #처음 마지막 다르다면
            print(words[i]+ "2")
            answer.append(i % n + 1)
            answer.append(i//n + 1)
            brek = True
            break
    
    if not brek:
        answer = [0,0]

    return answer
