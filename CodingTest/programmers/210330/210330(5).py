def panbyul(boarded):
    answer = True
    for line in boarded:
        for yoso in line:
            if yoso == 1:
                answer = False
    return answer

def overlapping(board, square):
    overlaped = []
    for line in range(len(board)):
        tempoline = []
        for yoso in range(len(board[0])):
            sumed=board[line][yoso] + square[line][yoso]
            tempoline.append(sumed)
        overlaped.append(tempoline)
    return overlaped

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
passed = False
#가로 길이
garolen = len(board[0])
serolen = len(board)
#최대 허용가능 정사각형
maxsqu = min(serolen,garolen)
#제일 큰놈
#사각형 만들기
rectan = []
kugi = range(maxsqu)
for i in kugi:
    line = []
    for j in kugi:
        line.append(1)
    rectan.append(line)
#겹치기
overlped = overlapping(rectan,board)
#판별하기
panbyul(overlped)
# print(panbyul(overlped))

#그다음 작은놈
rectan = []
kugi = range(maxsqu-1) #(0,0 부터 1,1 까지)
for i in kugi:
#이동하기

#제일 큰놈-1
#제일 큰놈-2
#.
#.
#.
#1까지
