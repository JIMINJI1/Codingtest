def solution(t, p):
    answer = 0
    p_len = len(p)
    p_value = int(p)
    
    for i in range(len(t)-p_len+1):
        num= int(t[i:i+p_len])
        if num<=p_value:
            answer+=1
    return answer