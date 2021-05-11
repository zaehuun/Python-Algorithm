#효율성 통과를 위해 공부 후 다시 풀어보기
#아래 코드는 정확성만 통과한 콛
#효율성 걸린 문제는 확실히 pop, append를 사용하면 안 될 거 같다.

# from collections import deque
# def solution(food_times, k):
#     answer = 0
#     food = deque([(i,food_times[i]) for i in range(len(food_times))])
#     while k:
#         if len(food) == 0:
#             return -1
#         num, time = food.popleft()
#         if time - 1> 0:
#             food.append((num,time-1))
#         k = k - 1
#     if len(food):
#         num , answer = food.popleft()
#         return num + 1
#     else:
#         return -1
