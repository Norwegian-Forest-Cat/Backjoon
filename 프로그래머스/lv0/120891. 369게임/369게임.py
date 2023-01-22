def solution(order):
    answer = 0
    clap = ['3', '6', '9']
    order = list(str(order))
    for i in range(len(order)):
        if order[i] in clap:
            answer += 1
    return answer