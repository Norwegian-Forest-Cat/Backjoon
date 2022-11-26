# 문자열 반복

N = int(input())
arr = [input().split() for _ in range(N)]

for data in arr:
    cnt = int(data[0])
    for i in range(len(data[1])):
        for _ in range(cnt):
            print(data[1][i], end='')
    print()