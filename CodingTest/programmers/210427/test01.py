a = [[7,1]]
print(a,id(a),id(a[0]))
for b in a:
    a.append([b[0],b[1]+1])
    a.pop(0)
print(a,id(a),id(a[0]))