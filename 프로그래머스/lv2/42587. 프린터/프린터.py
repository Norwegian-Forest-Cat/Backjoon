def solution(priorities, location):
    answer = 0      # 출력 횟수
    while 1:
        flag = 0
        # 우선순위 확인
        for i in range(1, len(priorities)):
            if priorities[i] > priorities[0]:
                flag = 1
        # 뒤에 우선순위가 높은 문서가 있을 경우 순서 변경
        if flag == 1:
            priorities.append(priorities[0])
            priorities.pop(0)
            if location == 0:
                location = len(priorities) - 1  # 맨 뒤로 이동
            else:
                location -= 1

        # 뒤에 우선순위가 높은 문서가 없음
        elif flag == 0:
            answer += 1
            if location == 0:
                return answer
            priorities.pop(0)
            location -= 1