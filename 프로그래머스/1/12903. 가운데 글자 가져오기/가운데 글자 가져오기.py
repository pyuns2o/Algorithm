import math

def solution(s):
    len_s = len(s)
    if len_s % 2 == 0:
        med = int(len_s / 2)
        return s[med-1:med+1]
    else:
        med = math.floor(len_s / 2)
        return s[med]