# 정확히 룩이 8개가 있어야 한다! -> 8개보다 없어도 no
T = int(input())
for TC in range(1, T + 1):
    arr = [input() for _ in range(8)]
    answer = 'yes'
    Rook = 0
    for x in range(8):      # 위에서 아래로 검사
        cnt = 0
        for y in range(8):
            if 'O' == arr[x][y]:
                cnt += 1
                Rook += 1       # Rook 개수는 1번만 확인한다.
        if cnt > 1:
            answer = 'no'
            break
    for y in range(8):      # 좌에서 우로 검사
        cnt = 0
        for x in range(8):
            if 'O' == arr[x][y]:
                cnt += 1
        if cnt > 1:
            answer = 'no'
            break

    if Rook != 8:       # Rook이 정확히 8개 있어야 통과이다.
        answer = 'no'
    print(f'#{TC} {answer}')