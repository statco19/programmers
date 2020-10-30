import heapq
def solution(operations):
    data_min, data_max = [], []
    heapq.heapify(data_min)
    heapq.heapify(data_max)
    
    for order in operations:
        if 'I' in order:
            num = int(order.split(' ')[-1])
            heapq.heappush(data_min,num)
            heapq.heappush(data_max,-num)
        if "D 1" == order and data_max and data_min:
            MAX = heapq.heappop(data_max)
            data_min.remove(-MAX)
        elif "D -1" == order and data_max and data_min:
            MIN = heapq.heappop(data_min)
            data_max.remove(-MIN)
    if not data_min:
        return [0,0]
    answer = [max(data_min), min(data_min)]
    
    return answer
