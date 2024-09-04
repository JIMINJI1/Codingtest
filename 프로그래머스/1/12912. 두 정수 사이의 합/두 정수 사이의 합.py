def solution(a, b):
    # answer = 0
    if a==b :
        return a
    
    min_val = min(a, b)
    max_val = max(a, b)
    
    return sum(range(min_val, max_val + 1))