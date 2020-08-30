//https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    answer = 0
    
    cities = list(map(lambda x : x.lower(), cities))
    if cacheSize == 0:
        return 5 * len(cities)
    cache = []
    cnt = 0
    
    for city in cities:
        if city not in cache:
            answer += 5
            if cnt == cacheSize :
                cache.pop(0)
                cache.append(city)
            else:
                cache.append(city)
                cnt += 1
        else:
            answer+=1
            tmp = cache.pop(cache.index(city))
            cache.append(tmp)
    #0. cache size가 0이면 내 코드랑 안 맞으니 예외로 뺌
    #1. 캐시에 있는지확인
    #2. 없으면 cache miss, +5, cache size 확인 후 pop 결정 후 cache에 추가
    #3, 있으면 +1, pop해서 맨 뒤에 append
    
    return answer
