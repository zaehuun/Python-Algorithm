def solution(s):
    dic = {"zero" : '0',"one" : "1", 'two' : '2', 'three' : '3', 'four' : '4',
          'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    answer = ""
    num = ""
    for i in s:
        if 'a' <= i <= 'z':
            num += i
            if num in dic:
                answer += dic[num]
                num = ''
        else:
            answer += i
    return int(answer)
