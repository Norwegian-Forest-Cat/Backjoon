# 팰린드롬수

while True:
    arr = list(map(int, input()))
    if arr == [0]:
        break

    answer = 'yes'
    N = len(arr)
    for i in range(int(N / 2)):
        if arr[i] != arr[-i-1]:
            answer = 'no'
    print(answer)