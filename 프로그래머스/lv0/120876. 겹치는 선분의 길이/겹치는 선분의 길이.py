# 선분을 bucket에 담아 겹치는 선분, 즉 bucket 2이상의 개수를 구한다.
def solution(lines):
    answer = 0
    lines.sort()
    bucket = [0] * 201      # -100 ~ 100 => 100 ~ 201
    
    # 선분 bucket에 담아 count 
    for i in range(3):
        if lines[i][1] > lines[i][0]:
            for j in range(lines[i][1] - lines[i][0]):
                bucket[j + lines[i][0] + 100] += 1      # 음수 때문에 + 100 
    
    # 겹치는 선분 확인
    for i in range(len(bucket)):
        if bucket[i] >= 2:
            answer += 1
    return answer 