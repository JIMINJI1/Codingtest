def solution(n):
    # 정수를 문자열로 변환하고, 내림차순으로 정렬한 후 리스트를 문자열로 합침
    sorted_str = ''.join(sorted(str(n), reverse=True))
    # 정수형으로 변환하여 반환
    return int(sorted_str)