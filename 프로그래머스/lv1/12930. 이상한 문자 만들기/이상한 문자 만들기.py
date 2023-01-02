def solution(s):
    arr = list(s)
    index = 0       # 홀짝을 비교하는 index
    for i in range(len(arr)):
        if arr[i] == ' ':
            index = 0       # 공백일 경우 index 초기화
        elif index % 2 == 0:
            arr[i] = arr[i].upper()
            index += 1
        else:
            arr[i] = arr[i].lower()
            index += 1

    answer = ''.join(s for s in arr)    # list -> str 변환
    return answer
