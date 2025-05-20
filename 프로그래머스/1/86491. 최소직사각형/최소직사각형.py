def solution(sizes):
    rotated = [(max(w, h), min(w, h)) for w, h in sizes]
    max_w = max([w for w,h in rotated])
    max_h = max([h for w,h in rotated])
    return max_w * max_h