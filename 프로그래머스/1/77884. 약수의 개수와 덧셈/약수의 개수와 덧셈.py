#제곱수로 홀,짝 판단해서 더하고 빼기
# i ** 0.5 => 제곱근 구함 
def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    
    return answer
