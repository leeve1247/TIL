#https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    temp = s.split(' ')
    temps = ''
    for word in temp:
        tempword = ''
        for i in range(len(word)):
            if i%2 == 0:
                tempword += word[i].upper()
            else:
                tempword += word[i].lower()
        temps += tempword + " "
    return temps[:-1]