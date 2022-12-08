def solution(prices):
    N = len(prices)
    bucket = [0] * N
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            cnt += 1
            if prices[i] > prices[j]:
                break
        bucket[i] += cnt
    return bucket

prices = [1, 2, 3, 2, 3]
print(solution(prices))