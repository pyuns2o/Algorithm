import heapq

def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙 (음수로 넣기)
    valid = [False] * len(operations)  # 유효성 표시

    for idx, op in enumerate(operations):
        if op.startswith("I"):  # 삽입 연산
            num = int(op.split()[1])
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx)) # 음수로 넣기
            valid[idx] = True

        elif op == "D 1":  # 최댓값 삭제
            while max_heap:
                value, i = heapq.heappop(max_heap)
                if valid[i]:
                    valid[i] = False
                    break

        elif op == "D -1":  # 최솟값 삭제
            while min_heap:
                value, i = heapq.heappop(min_heap)
                if valid[i]:
                    valid[i] = False
                    break

    # 유효한 최댓값 찾기
    max_val = None
    while max_heap:
        value, i = heapq.heappop(max_heap)
        if valid[i]:
            max_val = -value
            break

    # 유효한 최솟값 찾기
    min_val = None
    while min_heap:
        value, i = heapq.heappop(min_heap)
        if valid[i]:
            min_val = value
            break

    if max_val is None or min_val is None:
        return [0, 0]
    return [max_val, min_val]