def solution(num, total):
    for i in range(total + num, -total - num, -1):  # 뒤에서부터 확인한다.      
        answer = []
        for j in range(num):
            answer.append(i - j)
        if sum(answer) == total:
            answer.sort()
            return answer