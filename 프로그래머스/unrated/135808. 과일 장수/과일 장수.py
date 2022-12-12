def solution(k, m, score):
    score.sort(reverse=True)
    N = int(len(score) / m)     # 상자의 개수
    price = 0
    for i in range(N):
        fruit = score[m * i: m * (i + 1)]
        price += min(fruit) * m
    return price