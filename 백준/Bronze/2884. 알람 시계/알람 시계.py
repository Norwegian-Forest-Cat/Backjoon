# 알람 시계

hour, minute = map(int, input().split())
minute -= 45

if minute < 0:
    minute = 60 + minute
    if hour == 0:
        hour = 23
    else:
        hour -= 1
print(hour, minute)