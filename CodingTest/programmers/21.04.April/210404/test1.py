import calendar

def solution(a, b):
    list1 = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    weeks = calendar.weekday(2016,a,b)
    return list1[weeks]