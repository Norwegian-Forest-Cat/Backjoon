def dfs(level, arr, sumV):
    global maxV
    if len(arr) <= 2:
        maxV = max(maxV, sumV)
        return

    for i in range(len(arr) - 2):
        value = arr[i + 1]
        add = arr[i] * arr[i + 2]
        arr.pop(i + 1)
        dfs(level + 1, arr, sumV + add)
        arr.insert(i + 1, value)

N = int(input())
arr = list(map(int, input().split()))
maxV = 0
dfs(0, arr, 0)
print(maxV)