i = 2
v = 2
# while i <= 9:
#     while v <= 9:
#         print('{:>2} x {:>1} = {:>2}'.format(i, v, i*v), end=' ')
#         v += 1
#     print()
#     v = 2
#     i += 1

while i <= 9:
    while v <= 9:
        print('%dx%d=%2d' % (i, v, i*v), end=' ')
        v += 1
    print()
    v = 2
    i += 1