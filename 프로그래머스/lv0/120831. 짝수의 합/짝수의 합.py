def solution(n):
    answer = 0
    for i in range(1, n + 1):   # zero division 방지를 위해 1부터 시작
        if i % 2 == 0:
            answer += i
    return answer