a = [1,2]
n = 5
if n < 3:
    result = a[n-1]
else:
    count = 0
    while True:
        result = a[1]+a[0]
        a[0] = a[1]
        a[1] = result
        if n == count + 3:
            break
        count += 1
print(result)