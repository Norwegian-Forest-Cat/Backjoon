def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):
        num = str(num)
        for x in range(len(num)):
            if num[x] == str(k):
                answer += 1
    return answer