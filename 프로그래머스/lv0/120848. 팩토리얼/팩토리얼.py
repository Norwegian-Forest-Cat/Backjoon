def solution(n):
    i, total = 1, 1
    while total <= n:
        total *= i
        i += 1
    return i - 2