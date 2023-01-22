def solution(before, after):
    bucket = [1] * len(before)
    answer, N = 0, len(before)
    for i in range(N):
        for j in range(N):
            if bucket[j] == 1:
                if before[i] == after[j]:
                    bucket[j] = 0
                    break   # 해당 알파벳이 있으면 다음 알파벳 탐색을 위해 for문 이탈
    if sum(bucket) == 0:
        return 1
    return 0