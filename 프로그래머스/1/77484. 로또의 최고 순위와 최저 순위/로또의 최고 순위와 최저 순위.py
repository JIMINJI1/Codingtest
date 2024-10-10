def solution(lottos, win_nums):
    cnt = 0
    zero_cnt = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            cnt += 1
            
    max_rank = 7 - (cnt + zero_cnt)
    min_rank = 7 - cnt

    return [min(max_rank, 6), min(min_rank, 6)]
