def solution(n):
    n = str(n)
    n = list(n)
    answer = 0
    for i in range(len(n)):
        answer += int(n[i])
    return answer