# 숫자의 합

N = int(input())
arr = list(input())
for i in range(len(arr)):
    arr[i] = int(arr[i])
print(sum(arr))