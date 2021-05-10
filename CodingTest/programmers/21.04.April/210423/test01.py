def solution(lines):
    count = 1
    diglines = []
    for line in lines:
        ttime=line.split(' ')
        hms = ttime[1].split(':')
        endighms = (60*60*int(hms[0])+60*int(hms[1])+float(hms[2]))*1000 
        strdighms = endighms - (float(ttime[2][:-1])*1000) + 1
        diglines.append([int(strdighms),int(endighms)])
    for digline in diglines:
            p = digline[0]
            tcount = 0
            for a in diglines:
                if a[1] < p :
                    tcount += 0
                elif p - 999 < a[0]:
                    tcount += 0
                else:
                    tcount += 1
            if tcount > count :
                count = tcount        
            p += 1

            p = digline[1]
            tcount = 0
            for a in diglines:
                if a[1] < p :
                    tcount += 0
                elif p + 999 < a[0]:
                    tcount += 0
                else:
                    tcount += 1
            if tcount > count :
                count = tcount        
            p += 1  
    return count