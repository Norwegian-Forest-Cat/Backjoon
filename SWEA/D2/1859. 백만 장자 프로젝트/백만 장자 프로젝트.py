T = int(input())
for TC in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    gold = []       # 매입 가격을 저장하기 위해 리스트 사용
    answer = 0
    maxV = arr[-1]
    for i in range(N-1, -1, -1):    # 뒤에서 부터 탐색
        if arr[i] > maxV:       
            maxV = arr[i]
        else:
            answer += maxV - arr[i]

    print(f'#{TC} {answer}')