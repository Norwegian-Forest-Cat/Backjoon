# 국회의원 선거
from heapq import heappop, heappush, heapify

N = int(input())
heap = [int(input()) for _ in range(N)]
vote = heap[0]
heap.pop(0)     # 가장 앞 자리는 vote로 저장, heap에서 제거
cnt = 0         # 몇번 매수했는가?
if N > 1:
    for i in range(N - 1):      # 가장 작은수를 앞으로 위치하기 위해 음수로 변환
        heap[i] = heap[i] * -1
    heapify(heap)       # 음수로 변환 후 힙정렬

    while 1:    # 표 비교
        if vote > heap[0] * -1:
            break
        else:
            cnt += 1
            vote += 1
            current = heappop(heap)
            heappush(heap, current + 1)     # 현재 heap이 음수로 저장되어있으므로 + 1
    print(cnt)
else:
    print(0)