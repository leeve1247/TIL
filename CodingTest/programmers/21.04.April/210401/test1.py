#https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3

import re

def solution(new_id):
    oneRule = re.compile('[a-z0-9\-\_\.]')
    secReule = re.compile('\.\.')

    #1 대문자를 모두 소문자로 치환
    new_id=new_id.lower()

    #2 주어진 문자 제외 모든 문자 삭제
    uhyo=re.findall(oneRule,new_id)
    new_id = ""
    for yoso in uhyo:
        new_id += yoso

    #3 마침표 두개 이상 하나로
    while re.search(secReule,new_id) != None :
        loc = re.search(secReule,new_id).span()
        new_id = new_id[:loc[0]]+new_id[loc[1]-1:]

    #4 앞뒤 마침표 제거
    if new_id[0] == '.':
        new_id = new_id[1:]
    if new_id != "":
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    #5 빈 문자열이면 new_id에 a 대입
    if new_id == "" :
        new_id = 'a'

    #6 16자 이상이면 15문자만
    if len(new_id)>15:
        new_id = new_id[:15]

    #7 new_id의 길이가 2자 이하이면 new_id의 마지막 문자를 new_id 의 길이가 3이 될때까지 반복
    while len(new_id) < 3:
        new_id = new_id+new_id[-1]

    #8 뒤쪽 마침표 다시제거
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    return new_id