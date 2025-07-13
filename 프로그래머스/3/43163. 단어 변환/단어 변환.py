from collections import deque

def diff_one(word1, word2):
    diff = 0
    for a, b in zip(word1, word2):
        if a != b:
            diff += 1
        if diff > 1:
            return False
        
    return diff == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = set()
    q = deque()
    q.append((begin, 0))
    
    while q:
        cur_word, steps = q.popleft()
        
        if cur_word == target:
            return steps
        
        for next_word in words:
            if next_word not in visited and diff_one(cur_word, next_word):
                visited.add(next_word)
                q.append((next_word, steps + 1))
    
    return 0