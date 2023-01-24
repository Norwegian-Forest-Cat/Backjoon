def solution(numbers, direction):
    if direction == 'right':
        num = numbers[-1]
        numbers.pop()
        numbers.insert(0, num)  # 0번째 자리에 삽입
    elif direction == 'left':
        num = numbers[0]
        numbers.pop(0)
        numbers.append(num)
    return numbers