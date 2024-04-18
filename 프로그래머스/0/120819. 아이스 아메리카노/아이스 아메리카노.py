def solution(money):
    answer = []
    count_americano = money // 5500  
    change = money % 5500    

    answer.append(count_americano)   
    answer.append(change)    

    return answer
