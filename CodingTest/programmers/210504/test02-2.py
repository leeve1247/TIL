def suheng(w):
    result = ""
    if w == "":
        return ""
    else:
        u,v = divide(w)
        if iscorrect(u):
            result = u + suheng(v)
        else:
            result = edit(u,v)
    return result
        

def divide(w):
    u = ""
    v = ""
    temp = [0,0]
    for i in range(len(w)):
        if temp[0] != 0 and temp[0] == temp [1]:
            v = w[i:]
            break
        else:
            if w[i] == "(":
                temp[0] += 1
                u += w[i]
            else :
                temp[1] += 1
                u += w[i]
    return u,v

def iscorrect(string):
    if string == "":
        return True
    if string[0] == "(":
        return True
    else:
        return False
    
    
def edit(u,v):
    temp = "(" + suheng(v) + ")"
    for i in u[1:-1]:
        if i == "(":
            temp += ")"
        else:
            temp += "("
    return temp
    
    

def solution(p):
    answer = suheng(p)
    return answer