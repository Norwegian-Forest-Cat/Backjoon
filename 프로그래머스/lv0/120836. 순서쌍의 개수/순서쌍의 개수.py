def solution(n):
    answer = 0
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            if x * y > n:
                break
            elif x * y == n:
                answer += 1
    return answer