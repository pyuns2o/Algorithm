from collections import defaultdict

def solution(genres, plays):
    answer = []
    total = defaultdict(int)
    music = defaultdict(list)
    for i, gen in enumerate(genres):
        total[gen] += plays[i]
        music[gen].append((plays[i], i))
        
    genres_sorted = sorted(total.keys(), key=lambda g: total[g], reverse=True)
    
    for gen in genres_sorted:
        # 재생 수 내림차순
        # 고유변호 오름차순
        music[gen].sort(key=lambda x : (-x[0], x[1]))
        
        for play, idx in music[gen][:2]:
            answer.append(idx)
    return answer