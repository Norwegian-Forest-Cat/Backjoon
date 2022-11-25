# 평균
import statistics

N = int(input())
arr = list(map(int, input().split()))
M = max(arr)
for i in range(N):
    arr[i] = arr[i] / M * 100
    
print(statistics.mean(arr))
