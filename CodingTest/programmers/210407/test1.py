n=3
n3 = ""
while n>3:
    n3 = n3 + str(n%3)
    n = int(n/3)
n3=n3 + str(n)
kugi=len(n3)
sumed = 0
print(n3)
for i,v in enumerate(n3):
    sumed = sumed + int(v)*(3**(kugi-i-1))

print(sumed)
    
