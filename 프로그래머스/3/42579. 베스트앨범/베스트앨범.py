from collections import defaultdict

def solution(genres, plays):
    genre_total = defaultdict(int)
    for g, p in zip(genres, plays):
        genre_total[g] += p
    
    songs = [(i,g,p) for i, (g,p) in enumerate(zip(genres, plays))]
    
    songs.sort(key=lambda x: (-genre_total[x[1]], -x[2], x[0]))
    
    answer = []
    genre_count = defaultdict(int)
    for i,g, _ in songs:
        if genre_count[g] < 2:
            answer.append(i)
            genre_count[g] += 1
    return answer