def solution(my_string):
    answer = ''
    s = list(my_string)
    for i in range(len(s)):
        if s[i] not in answer:
            answer += s[i]    
    return answer