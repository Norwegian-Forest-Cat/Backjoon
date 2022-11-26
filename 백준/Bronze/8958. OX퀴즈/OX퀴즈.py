# OX 퀴즈

N = int(input())
total = [input() for _ in range(N)]
for arr in total:
    score = 0   # 점수 합계
    for i in range(len(arr)):
        for index in range(i, -1, -1):  # 연속된 O개수 확인
            if arr[index] == 'X':       # 연속된 정답이 끝나면 다음 점수 확인 
                break
            elif arr[index] == 'O':     # 연속된 정답이면 누적으로 점수 더하기
                score += 1
    print(score)