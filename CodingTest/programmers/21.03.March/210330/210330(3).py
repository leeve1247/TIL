strings=["abce", "abcd", "cdx"]
n = 2
strings.sort(key= lambda alphabet:alphabet[n]+alphabet)
print(strings)

strings=["sun", "bed", "car"]
n = 1
sstrings = []
answer = []
for word in strings:
    secndword = word[n]
    sstrings.append(secndword+word)
sstrings.sort()
for word in sstrings:
    temp = word[1:]
    answer.append(temp)
print(answer)


