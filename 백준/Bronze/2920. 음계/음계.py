# 음계

arr = list(map(int, input().split()))
cnt = 0
for i in range(1, 8):
    if arr[0] == 1:
        if arr[i] - arr[i - 1] == 1:
            cnt += 1
    elif arr[0] == 8:
        if arr[i - 1] - arr[i] == 1:
            cnt -= 1
if cnt == 7:
    print('ascending')
elif cnt == -7:
    print('descending')
else:
    print('mixed')