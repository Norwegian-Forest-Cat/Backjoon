def solution(my_string):
    answer = ''
    my_string = list(my_string)
    for i in range(len(my_string)):
        my_string[i] = my_string[i].lower()
    my_string.sort()
    for i in range(len(my_string)):
        answer += my_string[i]
    
    return answer