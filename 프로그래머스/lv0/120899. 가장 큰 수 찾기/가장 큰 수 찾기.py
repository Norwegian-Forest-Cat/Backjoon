def solution(array):
    answer = []
    answer.append(max(array))
    index = array.index(max(array))
    answer.append(index)
    return answer