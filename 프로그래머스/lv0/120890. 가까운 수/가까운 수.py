def solution(array, n):
    minV , minI = 100, 0
    array.sort()    # 가장 가까운 수가 여러 개일 경우 더 작은 수를 return하기 위해 정렬
    for i in range(len(array)):
        if abs(n - array[i]) < minV:
            minV = abs(n - array[i])
            minI = i
    return array[minI]