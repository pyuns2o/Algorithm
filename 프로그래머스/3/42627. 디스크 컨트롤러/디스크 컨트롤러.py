import heapq

def solution(jobs):
    jobs.sort()
    heap = []
    time = 0
    i = 0
    count = 0
    total = 0
    
    while count < len(jobs):
        while i < len(jobs) and jobs[i][0] <= time:
            request, duration = jobs[i]
            heapq.heappush(heap, (duration, request))
            i += 1
        
        if not heap:
            time = jobs[i][0]
        else:
            duration, request = heapq.heappop(heap)
            time += duration
            total += time - request
            count += 1
    return total // len(jobs)