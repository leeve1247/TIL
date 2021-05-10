def solution(n):
    n3 = ""
    while n>2:
        n3 = n3 + str(n%3)
        n = n//3
    n3=n3 + str(n)
    kugi=len(n3)
    sumed = 0
    for i,v in enumerate(n3):
        sumed = sumed + int(v)*(3**(kugi-i-1))
    return sumed