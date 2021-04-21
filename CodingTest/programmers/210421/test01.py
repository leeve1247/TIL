#https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3

def solution(user_id, banned_id):
    def test(user, banned): #필터링 여부 확인
        result = False
        if len(user) == len(banned):
            temp = ""
            for a in range(len(user)):
                if user[a] == banned[a]:
                    temp = temp + banned[a]
                else:
                    temp = temp + "*"
            if temp == banned:
                result = True
        return result

    listes = []
    listes.append(user_id)

    #문제 풀기
    for banned in banned_id:
        prd = [] #빈공간 구성
        for yuhu in listes: #단계별 삭제된 리스트 전개
            for a in range(len(yuhu)): #삭제된 리스트 별로 banned 필터링하는 걸 한개씩 만들기
                if test(yuhu[a],banned):
                    temp = yuhu[:]
                    temp.remove(yuhu[a])
                    prd.append(temp)
        listes = prd[:] #다음 단계 진행을 위한 리스트 업데이트 

    #중복 리스트 제거
    result = []
    for a in listes:
        if a not in result:
            result.append(a)

    return len(result)