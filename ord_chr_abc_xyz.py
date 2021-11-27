# A = ord('A')
a = ord('a')
# for i in range(A, A+26):
#     print(chr(i), end=' ')
string = ''
for i in range(a, a+26):
    string += str(chr(i))
    print(string)
