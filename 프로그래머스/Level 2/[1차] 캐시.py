def solution(cacheSize, cities):
    answer = 0
    for idx in range(len(cities)):
        cities[idx] = cities[idx].lower()
    #print(cities)
    cache = []
    if cacheSize == 0:
        return len(cities) * 5
    for city in cities:
        #print(cache)
        if len(cache) < cacheSize: #캐시 사이즈 여유있을 때
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
            else:
                cache.append(city)
                answer += 5
        else:
            if city in cache: #캐시에 있을 때
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
            else:
                if cache:
                    cache.pop(0)
                cache.append(city)
                answer += 5
    return answer
