def solution(n):
    answer = 0
    # 숫자를 문자열로 변환
    num_str = str(n)  
    
    for ch in num_str:
        answer += int(ch)
    return answer