# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
def solution(answers):
    questions = len(answers)
    answer, supo, count  = [],[],[]
    ptn = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(3):
        supo.append([])
        count.append(0)
    for j in range(3):
        for i in range(len(answers)):
            supo[j].append(ptn[j][i%len(ptn[j])])
    for j in range(3):        
        for i in range(len(answers)):
            if supo[j][i] == answers[i]:
                count[j] = count[j] +1
    for j in range(3):
        if count[j] == max(count):
            answer.append(j+1)
    
    return answer