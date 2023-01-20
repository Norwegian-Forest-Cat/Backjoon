# step = 1 : z 추가
# step = 2 : y 추가
# step = 3 : 연산자 추가
# step = 4 : x 추가
def solution(quiz):
    answer = []
    for i in range(len(quiz)):      # z, y, x 순서로 분해하기
        zyx = []
        step, end, cnt = 1, len(quiz[i]), 0
        for start in range(len(quiz[i]) - 1, -1, -1):   # 뒤 index부터 접근
            if step == 1:
                if quiz[i][start] == ' ':
                    zyx.append(quiz[i][start + 1:end])
                    step += 1
            elif step == 2:
                if cnt > 0 and quiz[i][start] == ' ':
                    zyx.append(quiz[i][start + 1:end])
                    step += 1
                elif quiz[i][start] == ' ':   # y의 end 세팅
                    cnt += 1
                    end = start
            elif step == 3:
                zyx.append(quiz[i][start])
                end = start - 1
                step += 1
            elif step == 4:
                zyx.append(quiz[i][0:end])
                break
        print(zyx)
        if zyx[2] == '+':
            if int(zyx[3]) + int(zyx[1]) == int(zyx[0]):    # index 역순 조심
                answer.append('O')
            else:
                answer.append('X')
        elif zyx[2] == '-':
            if int(zyx[3]) - int(zyx[1]) == int(zyx[0]):
                answer.append('O')
            else:
                answer.append('X')
    return answer