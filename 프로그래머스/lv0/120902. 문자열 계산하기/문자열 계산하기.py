
def solution(my_string):
    cal, index = [], -2     # 빈칸(' ') 처리를 위해 index 2단위 설정
    # 숫자 및 연산자 파싱
    for i in range(len(my_string)):
        if my_string[i] == '+':
            cal.append(int(my_string[index + 2:i - 1]))
            cal.append('+')
            index = i
        elif my_string[i] == '-' and my_string[i + 1] == ' ':   # 음수의 - 와 연산자 - 구분
            cal.append(int(my_string[index + 2:i - 1]))
            cal.append('-')
            index = i
    cal.append(int(my_string[index + 2:]))      # 추가하지 못한 남은 숫자 추가

    answer = int(cal[0])
    for i in range(1, len(cal), 2):
        if cal[i] == '+':
            answer += int(cal[i + 1])
        elif cal[i] == '-':
            answer -= int(cal[i + 1])
    return answer