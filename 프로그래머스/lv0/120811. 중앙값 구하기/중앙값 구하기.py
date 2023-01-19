def solution(array):
    if len(array) % 2 == 0:
        mid = int(len(array) // 2)
    else:
        mid = int(len(array) // 2)
    array.sort()
    return array[mid]