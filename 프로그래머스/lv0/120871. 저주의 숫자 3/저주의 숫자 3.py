# 3의 배수 또는 '3'이 포함될 경우 answer +=1을 해준다.
def solution(n):
    answer = 0

    for i in range(n):
        answer += 1
        while 1:    # while문 안에서 2 조건을 만족하도록 조정한다.
            if answer % 3 == 0:  # 3의 배수인 경우
                answer += 1
            elif '3' in str(answer):  # '3'을 포함하고 있는 경우
                answer += 1
            else:
                break
    return answer