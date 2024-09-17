def solution(sizes):
    answer =0
    max_w =0
    max_h =0
    
    for i in sizes:
        width = max(i)
        height = min(i)
        
        max_w = max(max_w,width)
        max_h = max(max_h,height)
        answer = max_w*max_h        
    return answer