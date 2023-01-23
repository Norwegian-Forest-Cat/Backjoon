def solution(chicken):

    service = 0
    while chicken >= 10:
        service += chicken // 10
        num = chicken // 10
        chicken = num + (chicken - num * 10)
    return service