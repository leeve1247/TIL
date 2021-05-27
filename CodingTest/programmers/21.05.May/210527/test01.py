#https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3
def solution(triangle):
    for i in range(len(triangle)):
        for j in range(i+1):
            if i == 0:
                continue
            elif i>0 and j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif i>0 and j==i:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
    answer = max(triangle[i])
    return answer