# 숫자의 개수

arr = [int(input()) for _ in range(3)]
result = 1
for number in arr:
    result *= number

result = list(str(result))  # count를 위해 list로 변경
bucket = [0] * 10
for i in range(len(result)):    # bucket에 count
    bucket[int(result[i])] += 1

for number in bucket:
    print(number)
    