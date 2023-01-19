def solution(my_string):
    answer = 0
    for word in my_string:
        if word.isdigit():
            answer += int(word)
    return answer