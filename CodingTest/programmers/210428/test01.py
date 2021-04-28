import heapq

def solution(scoville, K):
    minturn = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville)<=1 and scoville[0] < K:
            minturn = -1
            break
        if scoville[0]>=K:
            break
        temp1=heapq.heappop(scoville)
        temp2=heapq.heappop(scoville)
        temp = temp1 + temp2*2
        heapq.heappush(scoville,temp)
        minturn += 1
    
    return minturn