def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2 ,5]
    c = [3 ,3 ,1 ,1 ,2 ,2 ,4 ,4 ,5 ,5]
    
    score = [0] * 3
    answer=[]
    
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            score[0]+=1
        if answers[i] == b[i%len(b)]:
            score[1]+=1
        if answers[i] == c[i%len(c)]:  
            score[2]+=1
            
    max_score=max(score)
    
    for z in range(0,len(score)):
        if max_score == score[z]:
            answer.append(z+1)
            
    return answer
