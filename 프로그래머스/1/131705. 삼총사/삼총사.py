def solution(numbers):
    count = 0
    length = len(numbers)
    for i in range(length - 2): 
        for j in range(i + 1, length - 1):  
            for k in range(j + 1, length): 
                if numbers[i] + numbers[j] + numbers[k] == 0:
                    count += 1
    return count