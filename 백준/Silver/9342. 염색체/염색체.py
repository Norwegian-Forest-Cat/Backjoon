N = int(input())
arr = [list(input()) for _ in range(N)]
index = ['A', 'B', 'C', 'D', 'E', 'F']
condition = ['A', 'F', 'C']

for i in range(N):
    cnt = 0     # 규칙을 몇번 통과했는지 count

    if arr[i][0] in index:  # 첫번째 규칙
        cnt += 1
        if arr[i][0] not in condition:
            arr[i].pop(0)
        for j in range(3):
            if arr[i][0] == condition[j]:   # 2, 3, 4번째 규칙
                cnt += 1
                while len(arr[i]) > 0 and arr[i][0] == condition[j]:
                    arr[i].pop(0)
    if cnt == 4 and len(arr[i]) == 0:
        print('Infected!')
    elif cnt == 4 and len(arr[i]) == 1 and arr[i] in index:
        print('Infected!')
    else:
        print('Good')