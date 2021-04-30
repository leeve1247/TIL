def solution(name):
    named = list(name)
    cursor = 0
    sunser = []
    answer = 0
    alphabet = 'ABCDEFGHIJKLMNOPQRXTUVWXYZ'
    alphadic = {}
    for i in range(len(alphabet)):
        if i <= 13:
            alphadic[alphabet[i]] = i
        else :
            alphadic[alphabet[i]] = 26 - i
    for i in range(len(name)):
        answer += alphadic.get(name[i])

    named[cursor] = 'A'

    while True:
        if len(set(named)) == 1:
            break
        i = 0
        while i*2<=len(name):
            i += 1
            if named[(cursor + i)%len(name)] != 'A':
                cursor = (cursor + i)%len(name)
                answer += i
                named[cursor] = 'A'
                break
            if named[(cursor - i)%len(name)] != 'A':
                cursor = (cursor - i)%len(name)
                answer += i
                named[cursor] = 'A'
                break    
    return answer