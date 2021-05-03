def solution(name):
    answer = 0
    alphabet = 'ABCDEFGHIJKLMNOPQRXTUVWXYZ'
    alphadic = {}
    for i in range(len(alphabet)):
        if i <= 13:
            alphadic[alphabet[i]] = i
        else :
            alphadic[alphabet[i]] = 26 - i
    print(alphadic)
    for i in range(len(name)):
        answer += alphadic.get(name[i])
    answer += len(name)-1
    
    return answer