def solution(my_string):
    N = len(my_string) // 2
    my_string = list(my_string)
    for i in range(N):
        my_string[i], my_string[-1-i] = my_string[-1-i], my_string[i]
    answer = ''
    for i in range(len(my_string)):
        answer += my_string[i]
    return answer