# N = 1
# number = 1

# def calculate(s1,s2):
#     result = []
#     for a in s1:
#         for b in s2:
#             result.append(a + b)
#             result.append(a * b)
#             result.append(a - b)
#             if b != 0:result.append(int(a/b))
#     return result
# s = {}
# found = False
# for i in range(1,9):
#     s[i] = set()
#     yunsok = 0
#     for j in range(0, i):
#         yunsok += 10**j*N
#     s[i].add(yunsok)
#     if number in s[i]:
#         resultt = i
#         found = True
#         break

# if not found:
#     resultt = -1
#     for j in range(1,9):
#         for i in range(1,j):
#             s[j].update(calculate(s[i],s[j-i]))
#             if number in s[j]:
#                 resultt = j
#                 found = True
#                 break
#         if found :
#             break
for i in range(0,3):
    print(i)