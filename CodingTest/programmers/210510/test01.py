#https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3

def solution(arr1, arr2):
    answer = []
    rowlen = len(arr1)
    collen = len(arr1[0])
    for i in range(rowlen):
        answer.append([])
        for j in range(collen):
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer