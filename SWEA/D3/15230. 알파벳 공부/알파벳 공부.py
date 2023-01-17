T = int(input())
for TC in range(1, T + 1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    arr = input()
    answer = 0
    N = min(len(alphabet), len(arr))    # index error 방지
    for i in range(N):
        if alphabet[i] == arr[i]:
            answer += 1
        else:
            break       # 앞에서부터의 개수 확인, 뒤는 보면 안됨
    print(f'#{TC} {answer}')