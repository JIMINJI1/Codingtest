def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)
    
    for i in range(0, len(score), m):
        if i + m <= len(score):
            box = score[i:i+m]
            min_score = min(box)  
            answer += min_score * m 
            
    return answer
