#https://programmers.co.kr/learn/courses/30/lessons/64062?language=python3
# 이진 탐색 문제풀이
# 어떻게 풀것인가?
# 알맞은 result의 값은 1 이상 200000000 이하 (최대 징검다리 갯수가 200000개 이므로,)
# 만일 stones = [200000000] 일 경우, 200000000 명이 통과 가능
# result 의 값을 이진탐색 check, 범위 좁히기를 반복
def solution(stones, k):
    start = 1
    end = 200000000
    def islimited(stones,yesang,k):
        result = False
        count = 0
        for stone in stones:
            stone = stone - yesang
            if stone <= 0:
                stone = 0
                count = count + 1
            else:
                count = 0
            if count == k: #다음 사람이 건너지 못한다면
                result = True
                break
        return result

    yesang = int(start + (end-start)/2)
    while True:
        if islimited(stones,yesang,k):
            end = yesang
            yesang = int(start + (end-start)/2)
        else:
            start = yesang
            yesang = int(start + (end-start)/2)
        if start + 1 == end: #최종 결과
            result = end
            break
    return result