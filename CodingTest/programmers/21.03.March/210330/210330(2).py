numbers = [5, 0, 2, 7]

numbers.sort()
sumed = []
length = len(numbers)
print(length)
i = 0
j = 1
print(numbers)
while i < length-1 :
    while j < length :
        sumed.append(numbers[i]+numbers[j])
        print(sumed)
        j = j+1
    i = i+1
    j = i+1
    print(i)
    
sumed = set(sumed)
sumed = list(sumed)
sumed.sort()
answer = sumed

print(answer)