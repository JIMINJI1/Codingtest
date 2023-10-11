def solution(array, commands):
    answer = []
    for i, j, k in commands:
        s = sorted(array[i - 1:j])
        answer.append(s[k - 1])
    return answer