def solution(n):
    n = n ** (1 / 2)      # 루트로 나눔
    if n - n // 1 > 0:      # 소수점이 있다면
        return 2
    return 1        # 정수로 떨어진다면 True