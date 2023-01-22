def solution(numbers):
    answer = []
    alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    end = len(numbers)
    for start in range(len(numbers) - 3, -1, -1):  # 최소 3글자 이상이므로
        if numbers[start:end] in alpha:
            for i in range(10):
                if numbers[start:end] == alpha[i]:
                    answer.append(str(i))    # join을 위해 문자열로 저장
                    end = start
                    break
    answer.reverse()
    answer = ''.join(answer)
    return int(answer)  # 정수로 변환하여 출력