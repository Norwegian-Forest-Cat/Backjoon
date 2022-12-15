# 로또
from itertools import combinations

while 1:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    N = arr[0]
    arr.pop(0)
    for i in combinations(arr, 6):
        print(*list(i))
    print()