def solution(n, lost, reserve):
    answer = 0
    
    #도난당한 사람=여분있는 사람 
    new = set(lost) & set(reserve)
    
    #자기가 입어야 해서 제외 
    lost = sorted(set(lost) - new)
    reserve = set(reserve) - new 
    
    #빌려주기 본인+1, 본인-1꺼만 빌릴 수 있음
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer +=1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer +=1
            
    answer += n - len(lost)
    

    return answer