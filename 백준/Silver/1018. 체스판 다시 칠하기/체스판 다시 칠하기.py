# 체스판 다시 칠하기
# 체스판이 W로 시작 / W로 시작 2가지를 구분하여 확인해야 한다.

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
minV = 9999

# 8 * 8 배열 세팅
for x in range(0, N - 8 + 1):   # x 기준점
    for y in range(0, M - 8 + 1):   # y 기준점
        base = []
        for z in range(8):      # 기준점에서 8줄 추가
            base.append(arr[x + z][y: y + 8])

        # 배열이 세팅되면 색칠해야 할 개수 확인
        cntW, cntB = 0, 0  # 체스판이 W, B시작할때 각각 개수 확인
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:    # 체스판의 배열 switch 역할
                    if base[i][j] == 'W':
                        cntB += 1
                    elif base[i][j] == 'B':
                        cntW += 1
                else:
                    if base[i][j] == 'W':
                        cntW += 1
                    elif base[i][j] == 'B':
                        cntB += 1
        minV = min(minV, cntW, cntB)
print(minV)