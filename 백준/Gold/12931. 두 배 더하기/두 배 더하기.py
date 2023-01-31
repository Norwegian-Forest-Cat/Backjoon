# 반대로 생각하여 주어진 배열을 모두 0으로 만드는 최소 횟수를 계산한다.
N = int(input())
arr = list(map(int, input().split()))
cnt = 0

while sum(arr) > 0: # arr이 모두 0이 될때까지 반복
    check = 0
    for i in range(N):  # 전부 짝수인지 check
        if arr[i] % 2 == 0:
            check += 1

    if check == N:  # 전부 짝수일 경우 2로 나눠준다.
        for i in range(N):
            arr[i] = arr[i] // 2
        cnt += 1
    else:   # 홀수는 -1을 해준다.
        for i in range(N):
            if arr[i] % 2 != 0:
                arr[i] -= 1
                cnt += 1
print(cnt)