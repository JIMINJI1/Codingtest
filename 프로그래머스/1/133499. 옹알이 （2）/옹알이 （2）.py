def solution(babbling):
    baby = ["aya", "ye", "woo", "ma"]
    cnt = 0

    for word in babbling:
        is_valid = True
        for b in baby:
            # 같은 발음이 연속된 경우를 막기 위해 b가 두 번 연속되는지 확인
            if b * 2 in word:
                is_valid = False
                break
        if is_valid:
            # 네 가지 발음을 공백으로 대체해가며 검사
            for b in baby:
                word = word.replace(b, ' ')
            # 공백으로만 이루어졌는지 확인
            if word.strip() == '':
                cnt += 1

    return cnt
