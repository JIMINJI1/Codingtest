def solution(x):
    sumnumber = sum(int(i) for i in str(x))
    
    return x %sumnumber ==0