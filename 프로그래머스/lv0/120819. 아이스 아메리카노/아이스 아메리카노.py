def solution(money):
    N = money // 5500
    change = money - N * 5500
    return [N, change]