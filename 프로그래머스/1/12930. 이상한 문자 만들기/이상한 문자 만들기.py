def solution(s):
    words = s.split(" ")  
    answer = ''  

    for word in words:
        modified_word = ''  
        for i in range(len(word)):
            if i % 2 == 0:  
                modified_word += word[i].upper()  
            else:
                modified_word += word[i].lower() 
        answer += modified_word + ' '  

    return answer[:-1]  
