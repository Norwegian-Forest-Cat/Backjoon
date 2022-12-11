# 귤 고르기

def solution(k, tangerine):
    bucket = [0] * (max(tangerine) + 1)
    for i in range(len(tangerine)):
        bucket[tangerine[i]] += 1
    bucket.sort(reverse=True)
    answer = 0
    for i in range(len(bucket) - 1):    # 0은 확인하지 않으므로 -1
        k -= bucket[i]
        answer += 1
        if k <= 0:
            return answer