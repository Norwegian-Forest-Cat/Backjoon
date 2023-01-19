def solution(my_string):
    answer = ''
    for word in my_string:
        if word.isupper():
            answer += word.lower()
        elif word.islower():
            answer += word.upper()
    return answer