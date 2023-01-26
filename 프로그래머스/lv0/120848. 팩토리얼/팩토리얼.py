def solution(n):
    i, total = 1, 1
    while total <= n:
        total *= i
        i += 1
    return i - 2    # 이하이기 때문에 -1, while문 안에서 자동으로 +1이 되기 때문에 총 -2 추가