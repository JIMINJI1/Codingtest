def solution(n):
    sqrt = n **(0.5)
    if sqrt %1 ==0:
        return (sqrt+1)**2
    return -1