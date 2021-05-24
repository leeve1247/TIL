#https://programmers.co.kr/learn/courses/30/lessons/43236#
#assume 값이 클 경우 True, 그렇지 않으면 False
def isbig(distance, rocks, n, assume):
    #제거한 바위
    count = 0
    temp = 0
    for i in range(len(rocks)-1):
        if count > n:
            break
        temp += rocks[i+1]-rocks[i]
        if temp >= assume:
            temp = 0
        else:
            count += 1
    if count > n:
        result = True
    else:
        result = False
    return result



def solution(distance, rocks, n):
    #가정한 return값으로 바위를 제거해나갈 때, 제거한 바위가 n보다 많을 경우, 가정한 거리 최소가 너무 컸다.
    #가정한 return값으로 바위를 제거해나갈 때, 제거한 바위가 n보다 작거나 같을 경우, 가정한 거리의 최소가 너무 작거나 같았다.
    #distance를 우선 오름차순 정렬
    rocks.sort()
    rocks.append(distance)
    rocks.insert(0,0)
    maxr = distance+1
    minr = 1
    midr = int(((maxr-minr)/2) + minr)
    while True:
        if maxr == midr+1 and minr == midr:
            break
        yuhu = isbig(distance, rocks, n , midr)
        if yuhu:
            maxr = midr
            midr = int(((maxr-minr)/2) + minr)
        else:
            minr = midr
            midr = int(((maxr-minr)/2) + minr)
    answer = midr
    return answer