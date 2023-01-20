def solution(array):
    answer = 0
    for num in array:
        num = str(num)
        num = list(num)
        for i in range(len(num)):
            if num[i] == '7':
                answer += 1
    return answer