def solution(absolutes, signs):
    number = []
    for i in range(len(signs)):
        if signs[i]:  
            number.append(absolutes[i])
        else:  
            number.append(-absolutes[i])
            
    answer = sum(number)
    
    return answer
