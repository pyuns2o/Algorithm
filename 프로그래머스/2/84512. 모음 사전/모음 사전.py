from itertools import product

def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    dict = []
    
    for length in range(1,6):
        for comb in product(alpha, repeat=length):
            dict.append(''.join(comb))
            
    dict.sort()
    return dict.index(word) + 1