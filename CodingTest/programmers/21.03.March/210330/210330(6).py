def panbyul(board,kugi,xdot,ydot):
    answer = True
    for i in (xdot,xdot+kugi):
        for j in (ydot,ydot+kugi):
            try:
                if board[j][i] == 0:
                    answer = False
                else:
                    continue
            except IndexError:
                continue
    return answer

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
garolen = len(board[0])
serolen = len(board)
kugi = min(serolen,garolen)
answer = False
while kugi != 0:
    if answer == True:
        break
    for ydot in (0,serolen-kugi):
        if answer == True:
            break
        for xdot in (0,garolen-kugi):
            answer = panbyul(board,kugi,xdot,ydot)
            print(xdot,ydot,kugi,answer)
            if answer == True:
                thekugi = kugi
                break
    kugi = kugi - 1
print((kugi+1)**2)