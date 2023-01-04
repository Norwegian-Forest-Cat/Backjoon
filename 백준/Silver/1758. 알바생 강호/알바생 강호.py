N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)
tips = 0

for i in range(N):
    if arr[i] - i < 0:
        pass
    else:
        tips += (arr[i] - i)

print(tips)