#https://programmers.co.kr/learn/courses/30/lessons/64065?language=python3

def solution(s):
    processed = {}
    answer = []
    for a in s[2:-2].split('},{') :
        temp = list(map(int,a.split(',')))
        processed[len(temp)] = temp
    processed = sorted(processed.items())
    for a in processed:
        temp = [x for x in a[1] if x not in answer]
        answer.append(temp[0])
    return answer