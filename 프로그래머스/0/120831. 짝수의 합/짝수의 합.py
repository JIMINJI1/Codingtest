def solution(n):
    answer = 0
    for i in range(2, n+1, 2):  # 2부터 n까지 2씩 증가하면서 반복
        answer += i
    return answer