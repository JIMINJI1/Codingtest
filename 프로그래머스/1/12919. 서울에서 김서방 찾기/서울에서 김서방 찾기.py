def solution(seoul):
    answer = ''
    for i in range (0,len(seoul),1):
        if seoul[i] == "Kim":
            answer = "김서방은 {}에 있다".format(i)
    return answer