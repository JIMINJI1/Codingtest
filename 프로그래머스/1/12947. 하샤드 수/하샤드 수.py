def solution(x):
    sum_number = sum(int(i) for i in str(x))
    
    return x %sum_number ==0