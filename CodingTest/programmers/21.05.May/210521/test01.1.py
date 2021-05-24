#BFS 탐색

def solution(n, edge):
    nowvisited = set([1]) 
    while True:
        if edge == []:
            break
        temp = nowvisited
        nowvisited = set()
        for i in reversed(range(len(edge))):
            if edge[i][0] in temp:
                if not edge[i][1] in temp:
                    nowvisited.add(edge[i][1])
                del edge[i]
            elif edge[i][1] in temp:
                if not edge[i][0] in temp:
                    nowvisited.add(edge[i][0])
                del edge[i]
        #막판에 엉기는 경우 예외처리
        if len(nowvisited) != 0:
            answer = len(nowvisited)    
    return answer