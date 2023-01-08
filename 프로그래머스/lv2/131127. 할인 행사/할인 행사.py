# discount를 10개씩 잘라서 want의 개수만큼 있는지 비교

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - len(want)):  
        bucket = discount[i:i + 10]     # discount를 10개씩 bucket에 담아 확인
        index, cnt = 0, 0
        num = number[index]
        
        while index <= len(want):   # bucekt 확인 
            if num > 0:
                if want[index] in bucket:
                    bucket.remove(want[index])
                    cnt += 1
                    num -= 1
                else:
                    break
            else:
                index += 1
                if index < len(number):
                    num = number[index]
        if cnt == sum(number):
            answer += 1
    return answer