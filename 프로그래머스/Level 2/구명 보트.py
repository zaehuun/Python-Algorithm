# def solution(people, limit):
#     answer = 0
#     people.sort()
#     #50 50 70 80
#     while people:
#         min = people.pop()
#         for i in range(len(people)-1,-1,-1):
#             if people[i] + min <= limit:
#                 people.pop(i)
#                 break
#         answer += 1
#     return answer
#1차 코드 : 시간 초과 발생 / 이중 반복문에 pop(index)까지 있어서 발생하는 거 같다. / 입력 n이 많으니 한 번 훑는 식으로 코드 작성 해야곘다.

# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
#     while people:
#         #print(people)
#         min = people.pop(0)
#         if people and min + people[-1] <= limit:
#             people.pop()
#         answer += 1
#     return answer
#2차 코드 : 한 번 훑는 식으로 코드 작성했는데 시간 초과 발생 / 예전 어느 회사 코테처럼 효율성이 있는 문제들은 pop, remove, del 등 이런 함수들을 쓰면 시간 초과가 뜸
            #인덱싱으로 문제 풀어야 함.

  def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    while people:
        #print(people)
        min = people.pop(0)
        if people and min + people[-1] <= limit:
            people.pop()
        answer += 1
    return answer
