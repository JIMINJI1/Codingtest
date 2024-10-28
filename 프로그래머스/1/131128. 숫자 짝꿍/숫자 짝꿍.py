def solution(X, Y):
    # 각 숫자(0~9)의 개수를 저장할 리스트
    count_X = [0] * 10
    count_Y = [0] * 10

    # X와 Y의 각 숫자 카운트
    for digit in str(X):
        count_X[int(digit)] += 1

    for digit in str(Y):
        count_Y[int(digit)] += 1

    # 공통 숫자와 그 개수를 저장할 리스트
    commen_list = []

    # 공통 숫자를 찾아 추가
    for i in range(10):
        min_count = min(count_X[i], count_Y[i])
        commen_list.extend([str(i)] * min_count)

    # 공통 숫자가 없으면 -1 반환
    if not commen_list: 
        return "-1"

    # 공통 숫자를 내림차순으로 정렬
    commen_list.sort(reverse=True)
    answer = "".join(commen_list)

    # 모든 숫자가 0인 경우 0 반환
    if answer == "0" * len(answer):
        return "0"

    return answer
