def solution(k, score):
    k_score = []
    answer = []
    
    for i in score:
        k_score.append(i)
        if (len(k_score) > k):
            k_score.remove(min(k_score))
        answer.append(min(k_score))

    return answer