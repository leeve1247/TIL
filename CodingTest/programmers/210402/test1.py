#https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

def solution(board, moves):
    bucket = []
    count = 0
    for order in range(len(moves)):
        for floor in range(len(board)):
            catcher = board[floor][moves[order]-1]
            if catcher != 0:
                board[floor][moves[order]-1] = 0
                bucket.append(catcher)
                if len(bucket)>1:
                    if bucket[-1] == bucket[-2]:
                        bucket = bucket[:-2]
                        count = count + 2
                break
    return count