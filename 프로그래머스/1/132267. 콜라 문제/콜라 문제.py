def solution(a, b, n):
    total_bottles = n  
    total_cola = 0     
    
    while total_bottles >= a:
        new_cola = total_bottles // a * b
        
        total_cola += total_bottles // a * b
        
        remaining_bottles = total_bottles % a
        
        total_bottles = new_cola + remaining_bottles
    
    return total_cola
