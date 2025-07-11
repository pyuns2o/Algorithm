from itertools import permutations

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    permutation_set = set()
    
    for k in range(1, len(numbers) + 1):
        for p in permutations(numbers, k): #조합 생성
            num = int(''.join(p)) #문자열을 int형으로 변환
            permutation_set.add(num)
            
    count = sum(1 for n in permutation_set if is_prime(n))
    return count