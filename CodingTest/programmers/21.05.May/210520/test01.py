#https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3
#플로이드 와샬
def solution(n, results):
    #2차원 배열 구성 inf(1e5)과 1로 초기화
    infnum = int(1e9)
    match1 = []
    for i in range(n):
        match1.append([])
        for j in range(n):
            if i == j:
                match1[i].append(0)
            else:
                match1[i].append(infnum)
    for i in results:
        match1[i[0]-1][i[1]-1] = 1
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == k or j == k or i == j:
                    continue
                else:
                    match1[i][j] = min(match1[i][j],match1[i][k]+match1[k][j])
    for i in range(n):
        for j in range(n):
            if 0 < match1[i][j] < infnum:
                match1[j][i] = -1
                
    answer = 0
    for line in match1:
        if not infnum in line:
            answer += 1
    return answer