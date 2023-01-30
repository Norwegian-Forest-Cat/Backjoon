def solution(my_string):
    answer, start, end = 0, 0, 1
    for i in range(len(my_string) - 1):
        if my_string[i].isdigit() and my_string[i + 1].isdigit():
            end += 1
        elif my_string[i].isdigit():
            answer += int(my_string[start:end])
            start, end = i + 1, i + 2
        else:
            start += 1
            end += 1
    if my_string[start:end].isdigit():
        answer += int(my_string[start:end])
    
    return answer