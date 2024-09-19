def solution(strings, n):
    answer = []
    str_list=[]
    
    for i in range(len(strings)):
        str_list.append((strings[i][n], strings[i]))
    
    str_list.sort()
    
    for j in str_list:
        string = j[1]
        answer.append(string)
    return answer