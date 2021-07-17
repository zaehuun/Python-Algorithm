import heapq
def update(heap):
    arr = []
    for i in heap:
        heapq.heappush(arr,-i)
    return arr
def solution(operations):
    answer = [0,0]
    maxheap = []
    minheap = []
    for op in operations:
        c, num = op.split(" ")
        num = int(num)
        print(c,num)
        if c == 'I':
            heapq.heappush(minheap,num)
            heapq.heappush(maxheap,-num)
        else:
            if not maxheap:
                continue
            if num == 1:
                heapq.heappop(maxheap)
                minheap = update(maxheap)
            else:
                heapq.heappop(minheap)
                maxheap = update(minheap)
                
    print(maxheap,minheap)
    if not maxheap:
        return answer
    answer[0] = -heapq.heappop(maxheap)
    answer[1] = heapq.heappop(minheap)
    return answer
