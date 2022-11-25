# 단어 공부

arr = input().lower()
bucket = [0] * 150

# 문자 아스키코드 저장
for i in range(len(arr)):
    bucket[ord(arr[i])] += 1

# bucket 확인
count1, count2, maxV = 0, 0, ''
for cnt in range(len(bucket)):
    if bucket[cnt] > count1:
        count1 = bucket[cnt]
        maxV = chr(cnt).upper()
    elif bucket[cnt] == count1:
        count2 = bucket[cnt]

if count1 == count2:
    print('?')
else:
    print(maxV)