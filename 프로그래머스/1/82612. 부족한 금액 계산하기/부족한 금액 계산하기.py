def solution(price, money, count):
    total_cost=[]
    for i in range(1,count+1):
        cost = price*i
        total_cost.append(cost)
    if money-sum(total_cost)>=0:
        return 0
    else :
        return sum(total_cost)-money