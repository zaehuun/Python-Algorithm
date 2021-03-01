#https://programmers.co.kr/learn/courses/30/lessons/72410
#이렇게 푸는 게 맞는건가 싶을 정도로 노가다 느낌이 있다.

def solution(new_id):
    answer = ''
    new_id = new_id.lower() #1단계
    tmp_id = ""
    
    #2단계
    for i in new_id:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i =='.':
            tmp_id += i
    
    tmp_list = []
    
    #3단계
    for i in tmp_id:
        if not tmp_list:
            tmp_list.append(i)
        else:
            if tmp_list[-1] == '.' and i == '.':
                continue
            else:
                tmp_list.append(i)

    #4단계
    if len(tmp_list) > 0 and tmp_list[0] == '.':
        tmp_list.pop(0)
    if len(tmp_list) > 0 and tmp_list[-1] == '.':
        tmp_list.pop()
        
    #5단계
    if not tmp_list:
        tmp_list.append('a')
    
    if len(tmp_list) > 15:
        tmp_list = tmp_list[:15]
        if tmp_list[-1] == '.':
            tmp_list.pop()
    
    if len(tmp_list) <= 2:
        while len(tmp_list) != 3:
            tmp_list.append(tmp_list[-1])
    
        

    return ''.join(tmp_list)
