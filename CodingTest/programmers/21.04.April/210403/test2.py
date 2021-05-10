#https://programmers.co.kr/learn/courses/30/lessons/70128?language=python3


def solution(n, lost, reserve):
    for i in reserve:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)
            reserve.insert(0,-1)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
            reserve.remove(i)
            reserve.insert(0,-1)
    for i in reserve:
        if i+1 in lost:
            lost.remove(i+1)
            reserve.remove(i)
            reserve.insert(0,-1)

    result = n-len(lost)
    return result
